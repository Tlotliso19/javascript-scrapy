import scrapy
from three_websites.items import YahooFutures
from datetime import datetime, timedelta

today = datetime.now() 

yesterday= today-timedelta(days=1)
today_date=today.strftime('%Y/%m/%d')



class YahooFuturesSpider(scrapy.Spider):
    name = "Yahoo_futures"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/markets/commodities/"]

    def parse(self, response):
        yahoo_futures=YahooFutures()
        table_headings=response.css('table thead tr th div::text').getall()
        rows= response.css('table tbody tr')
        table_rows=[]
        for row in rows:
        # Extract text content from specific <td> elements
            symbol_index = row.css('td:nth-child(1) span div a div span::text').getall()  # First column
            name_index = row.css('td:nth-child(2) span div::text').getall()    # Second column
            price_index = row.css('td:nth-child(4) span div fin-streamer::text').getall()   # Fourth column
            market_time_index = row.css('td:nth-child(5) span::text').getall()  # Fifth column
            change_index = row.css('td:nth-child(6) span fin-streamer span::text').getall()   # Sixth column
            change_pecent_index = row.css('td:nth-child(7) span fin-streamer span::text').getall()   # Sixth column
            volume_index = row.css('td:nth-child(8) span fin-streamer::text').getall()  # Seventh column
            open_interest_index = row.css('td:nth-child(9) span::text').getall()  # Seventh column
    
            for symbol,name,price,market_time,change,change_pecent,volume,open_interest in zip(symbol_index,name_index,price_index,market_time_index,change_index,change_pecent_index,volume_index,open_interest_index):
                yahoo_futures['symbol']=symbol
                yahoo_futures['name']=name
                yahoo_futures['price']=price
                yahoo_futures['market_time']=market_time
                yahoo_futures['change']=change
                yahoo_futures['change_pecent']=change_pecent
                yahoo_futures['volume']=volume
                yahoo_futures['open_interest']=open_interest
                yahoo_futures['today_date']=today_date

                yield yahoo_futures
       

          

                
