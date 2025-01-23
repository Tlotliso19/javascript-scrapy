import scrapy
from scrapy_selenium import SeleniumRequest
from three_websites.items import GeneralEconomics,Comodities,Currencies,Bonds,Stocks,Crypto_1,Crypto_2


class FinancialPricesSpider(scrapy.Spider):
    name = "financial_prices"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/"]

    def start_requests(self):
        url = 'https://tradingeconomics.com/'
        # Use the correct syntax for passing the callback
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=3)
        
    def parse(self, response):

        links=response.css('#homematrix a::attr(href)').getall()
        metrix_icon_link=response.urljoin(links[-1])
        yield scrapy.Request(metrix_icon_link, callback=self.parse_metrix_page)

    def parse_metrix_page(self, response):
        navs=response.css('#pagemenutabs li a::attr(href)').getall()
        continent_names=response.css('#pagemenutabs li a::text').getall()
        for nav,continent_name in zip(navs,continent_names):
            countries_link=response.urljoin(nav)
            
            yield scrapy.Request(countries_link, callback=self.parse_country_link, meta={'continent_name': continent_name})  # Pass continent_name in meta
            
    def parse_country_link(self,response):
        economics_item = GeneralEconomics()
        table=response.css('table tr')
        first_heading_column=table[0].css('th span::text').getall()
        other_heading_columns=table[0].css('th::text').getall()
        other_heading_columns = [text.strip() if text.strip() else '' for text in other_heading_columns]
        heading=first_heading_column + other_heading_columns
        full_table=[]
        full_table.append(heading)
         # Retrieve the continent name from the meta attribute
        continent_name = response.meta.get('continent_name').strip()
        for row in table:
            first_body_column=row.css('td a::text').getall()
            other_body_columns=row.css('td::text').getall()
            other_body_columns=[text.strip() if text.strip() else '' for text in other_body_columns]
            row_entry=first_body_column + other_body_columns
            
            if len(row_entry)==10:
                economics_item["Country"]=row_entry[0] or ""
                economics_item["GDP"]=row_entry[1] or ""
                economics_item["GDP_Growth"]=row_entry[2] or ""
                economics_item["Interest_Rate"]=row_entry[3] or ""
                economics_item["Inflation_Rate"]=row_entry[4] or ""
                economics_item["Jobless_Rate"]=row_entry[5] or ""
                economics_item["Gov_Budget"]=row_entry[6] or ""
                economics_item["Debt_per_GDP"]=row_entry[7] or ""
                economics_item["Current_Account"]=row_entry[8] or ""
                economics_item["Population"]=row_entry[9] or ""
                economics_item['file_type']='csv'
                #full_table.append(row_entry)
                yield economics_item
            else:
                #print('######################################################')
                #print(row_entry)
                #print(len(row_entry))
                pass

            comodities_urls=response.css('.nav-dropdown-menu li a::attr(href)').getall()
            comodities_names=response.css('.nav-dropdown-menu li a::text').getall()
            for url,name in zip(comodities_urls,comodities_names):
                comodity_url=response.urljoin(url)
                comodity_name=name
                
                yield scrapy.Request(
                    url=comodity_url, 
                    callback=self.parse_comodities,
                    meta={'comodity_name':comodity_name}
                    )
                
    columns=["Country", "GDP", "GDP Growth", "Interest Rate", "Inflation Rate",
         "Jobless Rate", "Gov. Budget", "Debt/GDP", "Current Account", "Population"]
    def parse_comodities(self, response):
        comodity_name=response.meta.get('comodity_name').strip()
        
        if comodity_name == 'Currencies':
            tables = response.css('.card table')##get all tables 
            currencies=Currencies()
            for tbl in tables:
                table_heads = tbl.css('thead')
                table_bodies = tbl.css('tbody')
                if table_heads and table_bodies:
                   
            
                    for thead, tbody in zip(table_heads, table_bodies):# Iterate over the thead and tbody sections
                        rows= tbody.css('tr')
                        for row in rows:
                            name = row.css('td:nth-child(2) a b ::text').get()
                            price = row.css('td:nth-child(3) ::text').get()
                            day = row.css('td:nth-child(4) ::attr(data-value)').get()
                            pecentage = row.css('td:nth-child(5) ::attr(data-value)').get()
                            weekly = row.css('td:nth-child(6) ::attr(data-value)').get()
                            monthly = row.css('td:nth-child(7) ::attr(data-value)').get()
                            YTD =  row.css('td:nth-child(8) ::attr(data-value)').get()
                            YOY = row.css('td:nth-child(9) ::attr(data-value)').get()
                            date =  row.css('td:nth-child(10) ::text').get()
                            if name and price and day and pecentage and weekly and monthly and YTD and YOY and date:
                                
                                currencies['name'] = name.strip()
                                currencies['price'] = price.strip()
                                currencies['day'] = day.strip()
                                currencies['pecentage'] = pecentage.strip()
                                currencies['weekly'] = weekly.strip()
                                currencies['monthly'] = monthly.strip()
                                currencies['YTD'] =YTD.strip()
                                currencies['YOY'] = YOY.strip()
                                currencies['date'] =date.strip()
                                currencies['file_type']='csv'

                          
                          

                                yield currencies 
                          
                          
           
        elif comodity_name =='Stocks':
            tables = response.css('.card table')##get all tables 
            for tbl in tables:
                stocks=Stocks()
                table_heads = tbl.css('thead')
                table_bodies = tbl.css('tbody')
                if table_heads and table_bodies:
            
                    for thead, tbody in zip(table_heads, table_bodies):# Iterate over the thead and tbody sections
                        rows= tbody.css('tr')
                        for row in rows:
                            name = row.css('td:nth-child(2) a b ::text').get()
                            price = row.css('td:nth-child(3) ::text').get()
                            day = row.css('td:nth-child(4) ::attr(data-value)').get()
                            pecentage = row.css('td:nth-child(5) ::attr(data-value)').get()
                            weekly = row.css('td:nth-child(6) ::attr(data-value)').get()
                            monthly = row.css('td:nth-child(7) ::attr(data-value)').get()
                            YTD =  row.css('td:nth-child(8) ::attr(data-value)').get()
                            YOY = row.css('td:nth-child(9) ::attr(data-value)').get()
                            date =  row.css('td:nth-child(10) ::text').get()
                            if name and price and day and pecentage and weekly and monthly and YTD and YOY and date:
                                stocks['name'] = name.strip()
                                stocks['price'] = price.strip()
                                stocks['day'] = day.strip()
                                stocks['pecentage'] = pecentage.strip()
                                stocks['weekly'] = weekly.strip()
                                stocks['monthly'] = monthly.strip()
                                stocks['YTD'] = YTD.strip()
                                stocks['YOY'] = YOY.strip()
                                stocks['date'] = date.strip()
                                stocks['file_type'] = 'json'

                                yield stocks 
                                
                          
        elif comodity_name =='Commodities':
            tables = response.css('.card table')##get all tables 
            comodities=Comodities()
            for tbl in tables:
                table_heads = tbl.css('thead')
                table_bodies = tbl.css('tbody')
                if table_heads and table_bodies:
            
                    for thead, tbody in zip(table_heads, table_bodies):# Iterate over the thead and tbody sections
                        rows= tbody.css('tr')
                        for row in rows:
                            name = row.css('td:nth-child(1) a b ::text').get()
                            price = row.css('td:nth-child(2) ::text').get()
                            day = row.css('td:nth-child(3) ::attr(data-value)').get()
                            pecentage = row.css('td:nth-child(4) ::attr(data-value)').get()
                            weekly = row.css('td:nth-child(5) ::attr(data-value)').get()
                            monthly = row.css('td:nth-child(6) ::attr(data-value)').get()
                            YTD =  row.css('td:nth-child(7) ::attr(data-value)').get()
                            YOY = row.css('td:nth-child(8) ::attr(data-value)').get()
                            date =  row.css('td:nth-child(9) ::text').get()
                            if name and price and day and pecentage and weekly and monthly and YTD and YOY and date:
                                comodities['name'] = name.strip()
                                comodities['price'] =price.strip()
                                comodities['day']  = day.strip()
                                comodities['pecentage'] = pecentage.strip()
                                comodities['weekly'] = weekly.strip()
                                comodities['monthly']= monthly.strip()
                                comodities['YTD'] = YTD.strip()
                                
                                comodities['YOY'] = YOY.strip()
                                comodities['date'] = date.strip()
                                comodities['file_type'] = 'json'

                                yield comodities 
                           
                   
        
        elif comodity_name == 'Bonds':
            tables = response.css('.card table')##get all tables 
            bonds=Bonds()
            for tbl in tables:
                table_heads = tbl.css('thead')
                table_bodies = tbl.css('tbody')
                if table_heads and table_bodies:
            
                    for thead, tbody in zip(table_heads, table_bodies):# Iterate over the thead and tbody sections
                        rows= tbody.css('tr')
                        for row in rows:
                            name = row.css('td:nth-child(2) a b ::text').get()
                            yeild = row.css('td:nth-child(3) ::text').get()
                            day = row.css('td:nth-child(4) ::attr(data-value)').get()
                            
                            weekly = row.css('td:nth-child(5) ::attr(data-value)').get()
                            monthly = row.css('td:nth-child(6) ::attr(data-value)').get()
                            YTD =  row.css('td:nth-child(7) ::attr(data-value)').get()
                            YOY = row.css('td:nth-child(8) ::attr(data-value)').get()
                            date =  row.css('td:nth-child(9) ::text').get()
                            if name and yeild and day and  weekly and monthly and YTD and YOY and date:
                                bonds['name'] = name.strip()
                                bonds['yeild']  =yeild.strip()
                                bonds['day']  = day.strip()
                              
                                bonds['weekly']  = weekly.strip()
                                bonds['monthly']  = monthly.strip()
                                bonds['YTD']  = YTD.strip()
                                bonds['YOY'] = YOY.strip()
                                bonds['date']  =  date.strip()
                                bonds['file_type'] = 'json'

                                yield bonds 
                           
                         
          

        if  comodity_name == 'Crypto':
            tables = response.css('.card table')##get all tables 
            crypto_1=Crypto_1()
            crypto_2=Crypto_2()
            for tbl in tables:
                table_heads = tbl.css('thead')
                table_bodies = tbl.css('tbody')
                if table_heads and table_bodies:
            
                    for thead, tbody in zip(table_heads, table_bodies):# Iterate over the thead and tbody sections
                        rows= tbody.css('tr')
                        body_rows=tbody.css('tr')
                        column_count=""
                        for body_row in body_rows:
                            column_count=len(body_row.css('td'))
                            

                        
                        for row in rows:
                            
                            if column_count ==9:
                                
                                name = row.css('td:nth-child(1) a b ::text').get()
                                price = row.css('td:nth-child(2) ::text').get()
                                day = row.css('td:nth-child(3) ::attr(data-value)').get()
                                pecentage = row.css('td:nth-child(4) ::attr(data-value)').get()
                                weekly = row.css('td:nth-child(5) ::attr(data-value)').get()
                                monthly = row.css('td:nth-child(6) ::attr(data-value)').get()
                                YTD =  row.css('td:nth-child(7) ::attr(data-value)').get()
                                YOY = row.css('td:nth-child(8) ::attr(data-value)').get()
                                market_cap=''
                                date =  row.css('td:nth-child(9) ::text').get()
                             
                               
                                    

                            
                                if name and price and day and pecentage and weekly and monthly and YTD and YOY and date:
                                    
                                 
                                    crypto_2['name'] =name.strip()
                                    crypto_2['price'] = price.strip()
                                    crypto_2['day'] = day.strip()
                                    crypto_2['pecentage'] =pecentage.strip()
                                    crypto_2['weekly'] = weekly.strip()
                                    crypto_2['monthly'] = monthly.strip()
                                    crypto_2['YTD'] =YTD.strip()
                                    crypto_2['YOY'] = YOY.strip()
                                
                                    crypto_2['date'] = date.strip()
                                    crypto_2['file_type'] = 'csv' 
                                    yield crypto_2
                                    
                               
                                    
                            if column_count==10:
                                name = row.css('td:nth-child(1) a b ::text').get()
                                price = row.css('td:nth-child(2) ::text').get()
                                day = row.css('td:nth-child(3) ::attr(data-value)').get()
                                pecentage = row.css('td:nth-child(4) ::attr(data-value)').get()
                                weekly = row.css('td:nth-child(5) ::attr(data-value)').get()
                                monthly = row.css('td:nth-child(6) ::attr(data-value)').get()
                                YTD =  row.css('td:nth-child(7) ::attr(data-value)').get()
                                YOY = row.css('td:nth-child(8) ::attr(data-value)').get()
                                date =  row.css('td:nth-child(9) ::text').get()
                                market_cap=row.css('td:nth-child(9) ::attr(data-value)').get()
                                if name and price and day and pecentage and weekly and monthly and YTD and YOY and date and market_cap:
                            
                                    crypto_1['name'] =name.strip()
                                    crypto_1['price'] = price.strip()
                                    crypto_1['day'] = day.strip()
                                    crypto_1['pecentage'] =pecentage.strip()
                                    crypto_1['weekly'] = weekly.strip()
                                    crypto_1['monthly'] = monthly.strip()
                                    crypto_1['YTD'] =YTD.strip()
                                    crypto_1['YOY'] = YOY.strip()
                                    crypto_1['martket_cap'] = market_cap.strip()
                                    crypto_1['date'] = date.strip()
                                    crypto_1['file_type'] = 'json'
                             
                                    yield  crypto_1
                             
                        


        