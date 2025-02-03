# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass


class ThreeWebsitesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
columns=["Country", "GDP", "GDP Growth", "Interest Rate", "Inflation Rate",
          "Jobless Rate", "Gov. Budget", "Debt/GDP", "Current Account", "Population"]



class YahooFutures(scrapy.Item):
        symbol=scrapy.Field(serializer=str)
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=str)
        market_time=scrapy.Field(serializer=str)
        change=scrapy.Field(serializer=str)
        change_pecent= scrapy.Field(serializer=str)
        volume=scrapy.Field(serializer=str)
        open_interest=scrapy.Field(serializer=str)


class GeneralEconomics(scrapy.Item):
        Country =scrapy.Field(serializer=str)
        GDP=scrapy.Field(serializer=float)
        GDP_Growth=scrapy.Field(serializer=float)
        Interest_Rate=scrapy.Field(serializer=float)
        Inflation_Rate=scrapy.Field(serializer=float)
        Jobless_Rate=scrapy.Field(serializer=float)
        Gov_Budget=scrapy.Field(serializer=float)
        Debt_per_GDP=scrapy.Field(serializer=float)
        Current_Account=scrapy.Field(serializer=float)
        Population=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)



class CommoditiesPrices(scrapy.Item):
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        percentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)
        #to handle the general commodies

class Comodities(scrapy.Item): 
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        pecentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)


## to handle currencies data
class Currencies(scrapy.Item):
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        pecentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)



## to handle stock data


class Stocks (scrapy.Item):
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        pecentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)

## to handle bonds data


class Bonds (scrapy.Item):
        name=scrapy.Field(serializer=str)
        yeild=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)



## to handle crypto data
class Crypto_1 (scrapy.Item):
        name=scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        pecentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        martket_cap=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)



class Crypto_2(scrapy.Item):
        name= scrapy.Field(serializer=str)
        price=scrapy.Field(serializer=float)
        day=scrapy.Field(serializer=float)
        pecentage=scrapy.Field(serializer=float)
        weekly=scrapy.Field(serializer=float)
        monthly=scrapy.Field(serializer=float)
        YTD=scrapy.Field(serializer=float)
        YOY=scrapy.Field(serializer=float)
        date=scrapy.Field(serializer=str)
        today_date=scrapy.Field(serializer=str)

