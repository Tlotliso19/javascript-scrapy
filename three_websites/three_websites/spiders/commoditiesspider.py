import scrapy
from three_websites.items import CommoditiesPrices
from datetime import datetime, timedelta

today = datetime.now() 

yesterday= today-timedelta(days=1)
today_date=today.strftime('%Y/%m/%d')


class CommoditiesspiderSpider(scrapy.Spider):
    name = "commoditiesspider"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/commodities"]

    def parse(self, response):
        comodities_prices=CommoditiesPrices()
        table_rows=response.css('table tbody tr')
        for row in table_rows:
            if row:
                names=row.css('td:nth-child(1) a b::text').getall()
                prices=row.css('td:nth-child(2)::text').getall()
                days=row.css('td:nth-child(3)::attr(data-value)').getall()
                
                percentages=row.css('td:nth-child(4)::text').getall()
                weeklys=row.css('td:nth-child(5)::text').getall()
                monthlys=row.css('td:nth-child(6)::text').getall()
                YTDs=row.css('td:nth-child(7)::text').getall()
                YOYs=row.css('td:nth-child(8)::text').getall()
                dates=row.css('td:nth-child(9)::text').getall()
                for name,price,day,percentage,weekly,monthly,YTD,YOY,date in zip(names,prices,days,percentages,weeklys,monthlys,YTDs,YOYs,dates):
                    
                    comodities_prices['name']=name.strip()
                    comodities_prices['price']=price.strip()
                    comodities_prices['day']=day.strip()
                    comodities_prices['percentage']=percentage.strip()
                    comodities_prices['weekly']=weekly.strip()
                    comodities_prices['monthly']=monthly.strip()
                    comodities_prices['YTD']=YTD.strip()
                    comodities_prices['YOY']=YOY.strip()
                    comodities_prices['date']=date.strip()
                    comodities_prices['today_date']=today_date
                    yield comodities_prices
        else:
            pass
            ##yield{
                ##'nothing':'there is nothing'}

