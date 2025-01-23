# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreeWebsitesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
columns=["Country", "GDP", "GDP Growth", "Interest Rate", "Inflation Rate",
          "Jobless Rate", "Gov. Budget", "Debt/GDP", "Current Account", "Population"]
class GeneralEconomics(scrapy.Item):
    Country = scrapy.Field()  # Field for country
    GDP=scrapy.Field()
    GDP_Growth=scrapy.Field()
    Interest_Rate=scrapy.Field()
    Inflation_Rate=scrapy.Field()
    Jobless_Rate=scrapy.Field()
    Gov_Budget=scrapy.Field()
    Debt_per_GDP=scrapy.Field()
    Current_Account=scrapy.Field()
    Population=scrapy.Field()
    file_type=scrapy.Field()

##to handle the general commodies
class Comodities(scrapy.Item): 
        name=scrapy.Field()
        price=scrapy.Field()
        day=scrapy.Field()
        pecentage=scrapy.Field()
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()

## to handle currencies data
class Currencies(scrapy.Item):
        name=scrapy.Field()
        price=scrapy.Field()
        day=scrapy.Field()
        pecentage=scrapy.Field()
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()


## to handle stock data
class Stocks (scrapy.Item):
        name=scrapy.Field()
        price=scrapy.Field()
        day=scrapy.Field()
        pecentage=scrapy.Field()
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()
## to handle bonds data
class Bonds (scrapy.Item):
        name=scrapy.Field()
        yeild=scrapy.Field()
        day=scrapy.Field()
       
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()

## to handle crypto data
class Crypto_1 (scrapy.Item):
        name=scrapy.Field()
        price=scrapy.Field()
        day=scrapy.Field()
        pecentage=scrapy.Field()
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        martket_cap=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()

class Crypto_2(scrapy.Item):
        name=scrapy.Field()
        price=scrapy.Field()
        day=scrapy.Field()
        pecentage=scrapy.Field()
        weekly=scrapy.Field()
        monthly=scrapy.Field()
        YTD=scrapy.Field()
        YOY=scrapy.Field()
        date=scrapy.Field()
        file_type=scrapy.Field()
