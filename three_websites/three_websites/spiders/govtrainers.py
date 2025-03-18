import scrapy
import scrapy
from scrapy_selenium import SeleniumRequest
from three_websites.items import GeneralEconomics,Comodities,Currencies,Bonds,Stocks,Crypto_1,Crypto_2

class GovtrainersSpider(scrapy.Spider):
    name = "govtrainers"
    allowed_domains = ["training.gov.au"]
    start_urls = ["https://training.gov.au/"]

    def start_requests(self):
        url = 'https://training.gov.au/'
        # Use the correct syntax for passing the callback
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=3)
        
    def parse(self, response):
        print('*******************************************************************')
        print(response.url)
        print(response)