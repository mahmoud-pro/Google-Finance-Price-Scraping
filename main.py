import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    usd_price: float = 0

    def __post_init__(self):
        price_information = price_info(self.ticker, self.exchange)
        if price_information["ticker"] == self.ticker:
            self.price = price_information["price"]
            self.currency = price_information["currency"]
            self.usd_price = price_information["usd_price"]


@dataclass
class Position:
    stock: Stock
    quantity: int


@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        total_value = 0

        for position in self.positions:
            total_value += position.quantity * position.stock.usd_price
        return round(total_value, 2)


def create_request(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/111.0.0.0 Safari/537.36"}
    request = r.get(url, headers=headers)
    return request


def get_fx_to_usd(currency):
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    response = create_request(url)
    soup = BeautifulSoup(response.content, parser="lxml", features="lxml")

    fx_rate = soup.find("div", attrs={"data-last-price": True})
    amount = float(fx_rate["data-last-price"])

    return amount


def price_info(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = create_request(url)
    soup = BeautifulSoup(response.content, parser="lxml", features="lxml")

    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    usd_price = price
    if currency != "USD":
        usd_price = round(price * get_fx_to_usd(currency), 2)

    return {"ticker": ticker, "exchange": exchange, "price": price, "currency": currency, "usd_price": usd_price}


if __name__ == "__main__":
    # print(price_info("GOOGL", "NASDAQ"))
    # print(price_info("AMZN", "NASDAQ"))
    # print(price_info("SHOP", "TSE"))
    # print(price_info("SHOP", "NYSE"))
    # print(get_fx_to_usd("CAD"))
    # print(Stock("SHOP", "TSE"))

    shop = Stock("SHOP", "TSE")
    google = Stock("GOOGL", "NASDAQ")
    amazon = Stock("AMZN", "NASDAQ")
    shop_nyse = Stock("SHOP", "NYSE")

    portfolio = Portfolio([Position(google, 5),
                           Position(shop, 5),
                           Position(amazon, 5),
                           Position(shop_nyse, 5)])
    print(portfolio.get_total_value())
