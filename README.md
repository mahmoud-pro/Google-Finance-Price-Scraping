### Google Finance Price Scraping
* Scrape price information from Google Finance.
* Summarize portfolio valuation from an arbitrary number of positions.
* Solution reflect USD amount only, but also support positions listed in other currencies and support some sort of EX-ing capability.

### Exampls
    shop = Stock("SHOP", "TSE")
    google = Stock("GOOGL", "NASDAQ")
    amazon = Stock("AMZN", "NASDAQ")
    shop_nyse = Stock("SHOP", "NYSE")
    bns = Stock("BNS", "TSE")
    tesla = Stock("TSLA", "NASDAQ")

    portfolio = Portfolio([Position(google, 56),
                           Position(shop, 312),
                           Position(amazon, 435),
                           Position(shop_nyse, 708),
                           Position(tesla, 1530)])
    display_portfolio_summary(portfolio)

## Output
    +----------+------------+------------+---------+----------------+----------------+
    | Ticker   | Exchange   |   Quantity |   Price |   Market Value |   % Allocation |
    |----------+------------+------------+---------+----------------+----------------|
    | TSLA     | NASDAQ     |       1530 |  180.13 |      275598.90 |          74.51 |
    | AMZN     | NASDAQ     |        435 |   98.95 |       43043.25 |          11.64 |
    | SHOP     | NYSE       |        708 |   44.68 |       31633.44 |           8.55 |
    | SHOP     | TSE        |        312 |   44.56 |       13902.72 |           3.76 |
    | GOOGL    | NASDAQ     |         56 |  101.62 |        5690.72 |           1.54 |
    +----------+------------+------------+---------+----------------+----------------+
    Total portfolio value: $369,869.03

### Author
> Created by **Mahmoud Taha**
> 
<sub>for more information contact me.</sub>
