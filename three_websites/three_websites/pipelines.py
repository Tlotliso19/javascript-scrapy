# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from three_websites.items import GeneralEconomics 
import csv
import psycopg2
import json
from scrapy.utils.project import get_project_settings
import os
import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv
from pymongo import MongoClient


# Get today's date
today_date = datetime.date.today()

class YahooFutures:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Check if 'open_interest' exists
        if adapter.get('open_interest'):

            open_interest = adapter['open_interest']
            
            # Check if the 'open_interest' value contains 'M' for millions
            if 'M' in open_interest:
                print('*********************************************************************')
                print('M  EXCISITS')
                try:
                    # Remove 'M' and convert to float, then multiply by 10 million
                    adapter['open_interest'] = float(adapter['open_interest'].strip('M')) * 1000000
                    print(adapter['open_interest'])
                except ValueError:
                    # Handle case where conversion fails
                    adapter['open_interest'] = None
                    spider.logger.error(f"Invalid open_interest value: {open_interest}")
            
            # Handle other units like 'B' for billions if needed
            elif 'B' in open_interest:
                try:
                    # Remove 'B' and convert to float, then multiply by 1 billion
                    adapter['open_interest'] = float(open_interest.strip('B')) * 1000000000
                except ValueError:
                    adapter['open_interest'] = None
                    spider.logger.error(f"Invalid open_interest value: {open_interest}")

          # Check if 'volumnt exists
        if adapter.get('volume'):

            volume=adapter['volume']
            
            # Check if the 'open_interest' value contains 'M' for millions
            if 'M' in volume:
                print('*********************************************************************')
                print('M  EXCISITS')
                try:
                    # Remove 'M' and convert to float, then multiply by 10 million
                    adapter['volume']= float(adapter['open_interest'].strip('M')) * 1000000
                    print(adapter['volume'])
                except ValueError:
                    # Handle case where conversion fails
                    adapter['volume'] = None
                    spider.logger.error(f"Invalid open_interest value: {volume}")
            
            # Handle other units like 'B' for billions if needed
            elif 'B' in volume:
                try:
                    # Remove 'B' and convert to float, then multiply by 1 billion
                    adapter['volume'] = float(open_interest.strip('B')) * 1000000000
                except ValueError:
                    adapter['volume']=None
                    spider.logger.error(f"Invalid open_interest value: {volume}")
        return item








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

'''
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

        return item'''




class SaveToPostgresql:
    def __init__(self,PostgreSQL_url):
        self.connection_string='postgresql://postgres:hFDuugXn18Z3DBc8@inscrutably-distinct-garpike.data-1.use1.tembo.io:5432/postgres'
        self.name_set = set()  # To track processed item classes


    @classmethod
    def from_crawler(cls,spider):
        return cls(
            PostgreSQL_url=spider.settings.get("POSTGRESQL_URL"),
            
        )


    def open_spider(self, spider):
        # The open_spider method only needs the spider argument
        connection_string = self.connection_string
        #connection_string = "postgresql://erik_user:vJnjEibIrqr3BkvAwmjcZdbUiFi4oXfK@dpg-ctuh0f8gph6c73eqljrg-a.oregon-postgres.render.com/erik"
        print('##################################')
        print(connection_string)
        print('*****************************************************')
        url = urlparse(connection_string)

        # Database configuration extracted from URL
        db_config = {
            "host": url.hostname,
            "port": url.port,
            "database": url.path[1:],  # Skip the leading "/"
            "user": url.username,
            "password": url.password,
        }

        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # Clean up the connection when the spider finishes
        if hasattr(self, 'conn') and self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item,dict):
            print('*******************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*******************************')
            print(item)
        # Dynamically get the item class name
        name = type(item).__name__

        # Process each item class only once
        if name not in self.name_set:
            self.name_set.add(name)

            # Get the item field names and types
            columns = {}
            adapter = ItemAdapter(item)
            for field_name, field_meta in item.fields.items():
                # Get the serializer or use 'Unknown' if not available
                field_type = field_meta.get('serializer', 'Unknown')
                columns[field_name] = field_type

            # Build the column definitions for the CREATE TABLE query
            column_definitions = ", ".join([f"{field} {self.map_field_type(field_type)}" for field, field_type in columns.items()])

            # Reconnect to PostgreSQL and create the table for this item type
            self.create_table(name, column_definitions)

        # Now call insert_one to insert the item into the database
        self.insert_one(item, type(item).__name__)

        return item

    def insert_one(self, item, table_name):
        # Create the SQL insert query
        columns = ", ".join(item.fields.keys())
        values = ", ".join([f"%s" for _ in item.fields])  # Create a placeholder for each field value

        # Prepare the insert statement
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        # Extract the values from the item
        values_to_insert = [item[field] for field in item.fields]

        try:
            # Execute the insert query with the values
            self.cursor.execute(insert_query, values_to_insert)
            print(f"Inserted item into {table_name}")

        except psycopg2.Error as e:
            print(f"Error inserting item into {table_name}: {e}")

    def create_table(self, table_name, column_definitions):
        try:
            # Create the table if it doesn't exist
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    {column_definitions}
                );
            """
            self.cursor.execute(create_table_query)
            print(f"Table {table_name} created or already exists.")

        except psycopg2.Error as e:
            print(f"Error creating table {table_name}: {e}")

    def map_field_type(self, field_type):
        """Maps Python field types to PostgreSQL types"""
        field_type_mapping = {
            'str': 'TEXT',
            'int': 'INTEGER',
            'float': 'FLOAT',
            'bool': 'BOOLEAN',
            'datetime': 'TIMESTAMP',
            'Unknown': 'TEXT',  # Default type
        }
        return field_type_mapping.get(field_type, 'TEXT')  # Default to TEXT if not found

        
