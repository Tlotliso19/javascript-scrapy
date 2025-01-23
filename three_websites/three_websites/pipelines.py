# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from three_websites.items import GeneralEconomics 
import csv
import json
from scrapy.utils.project import get_project_settings
import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient


# Get today's date
#today_date = datetime.date.today()



class ThreeWebsitesPipeline:
    def process_item(self, item, spider):
        return item

 # Make sure to import the GeneralEconomics item class

class GeneralEconomicsCleaner:
    def process_item(self, item, spider):
        # Check if the item is an instance of GeneralEconomics
        if isinstance(item, GeneralEconomics):
            # Use ItemAdapter to access the item fields
            adapter = ItemAdapter(item)
            
            # Clean 'Country' field by stripping leading/trailing spaces
            if adapter.get('Country'):
                adapter['Country'] = adapter['Country'].strip()
            
            # Ensure that 'GDP_Growth' is not empty and provide a default if missing
            if not adapter.get('GDP_Growth'):
                adapter['GDP_Growth'] = 'Data not available'
            
            # Add any more data cleaning or transformations as necessary:
            # Example: Set a default value for 'GDP' if it’s missing
            if not adapter.get('GDP'):
                adapter['GDP'] = 'Data not available'
            

            # Return the cleaned item
            return item
        
        # If the item is not of the correct type, return it unchanged
        return item
    


mongo_uri='mongodb+srv://tlotlisoem:tlotliso19@cluster0.93oee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'


#from pymongo.errors import ConnectionError, OperationFailure


from pymongo.errors import OperationFailure


class SaveToMongoDB:

    collection_name = "homr"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.name = None
        self.document = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db]
        except Exception as e:
            spider.logger.error(f"Error connecting to MongoDB: {e}")
            raise

    def close_spider(self, spider):
        today_date = datetime.date.today()
        data = {
            "name": self.name,
            "date": str(today_date),
            "items": self.document
        }

        try:
            self.db[self.collection_name].insert_one(data)
            spider.logger.info(f"Inserted {len(self.document)} items into MongoDB.")
        except OperationFailure as e:
            spider.logger.error(f"Error inserting items into MongoDB: {e}")
        except Exception as e:
            spider.logger.error(f"Unexpected error: {e}")
        finally:
            self.client.close()
   
        

    def process_item(self, item, spider):
        
        self.document.append(ItemAdapter(item).asdict())
        # today_date = datetime.now().strftime("%Y-%m-%d")  Current date in YYYY-MM-DD format
        self.name = item.__class__.__name__

        return item

