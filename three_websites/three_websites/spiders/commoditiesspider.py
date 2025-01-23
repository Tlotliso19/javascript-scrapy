import scrapy


class CommoditiesspiderSpider(scrapy.Spider):
    name = "commoditiesspider"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/commodities"]

    def parse(self, response):
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
                    entry=name.strip(),price.strip(),day.strip(),percentage.strip(),weekly.strip(),monthly.strip(),YTD.strip(),YOY.strip(),date.strip()
                    yield{
                    'entry':entry
                    }
        else:
            yield{
                'nothing':'there is nothing'
            }

