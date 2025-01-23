'''from astrapy import DataAPIClient
import json
import datetime   # This will be needed later
import os

from dotenv import load_dotenv
from pymongo import MongoClient

with open('json/Bonds2000-200-200.json') as file:
    data = json.load(file)

# Load config from a .env file:
load_dotenv()
try:
  MONGODB_URI = 'mongodb+srv://tlotlisoem:tlotliso19@cluster0.93oee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

  # Connect to your MongoDB cluster:
  client = MongoClient(MONGODB_URI)
  database = client['homr']
  collection = database['homr']

  client.close()
except Exception as e:
  print(f"Error: {e}")

result = collection.insert_many(data)
print(result.acknowledged)'''


'''
class CustomSave:

    def process_item(self, item, spider):
        class_name = item.__class__.__name__

        # Define the directory where the file should be saved
        directory = r'C:\Users\tlotliso.makoboshane\projects\javascript-scrapy\three_websites\three_websites\spiders'
        
        if 'file_type' in item:
            file_type = item['file_type']

            # Handle CSV file saving
            if file_type == 'csv':
                # Use class name for the file name
                file_name = class_name +str(today_date) + '.csv'
                file_path = os.path.join(directory, 'csv', file_name)

                # Ensure the directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                # Convert item to dictionary using ItemAdapter
                adapter = ItemAdapter(item)
                item_dict = adapter.asdict()  # Convert to dictionary

                # Check if the file already exists to determine whether to write headers
                file_exists = os.path.exists(file_path)

                # Writing to CSV
                try:
                    with open(file_path, mode='a', newline='') as file:
                        writer = csv.writer(file)

                        # Write header only if the file is new (doesn't exist)
                        if not file_exists:
                            writer.writerow(item_dict.keys())  # Write header (keys of the dictionary)

                        # Write item values (values of the dictionary)
                        writer.writerow(item_dict.values())
                except Exception as e:
                    spider.logger.error(f"Error writing CSV file {file_path}: {e}")

            # Handle JSON file saving
            elif file_type == 'json':
                # Use class name for the file name
                file_name = class_name +str(today_date) + '.json'
                file_path = os.path.join(directory, 'json', file_name)

                # Ensure the directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                # Convert item to dictionary using ItemAdapter
                adapter = ItemAdapter(item)
                item_dict = adapter.asdict()

                # Writing to JSON
                try:
                    with open(file_path, mode='a', newline='') as file:
                        # If file is new, write the opening bracket for JSON array
                        if os.path.getsize(file_path) == 0:
                            file.write('\n')

                        # Write the item as a JSON object, adding a comma if it's not the first entry
                        json.dump(item_dict, file, ensure_ascii=False, indent=4)

                        # Add a trailing comma, except for the last item
                        file.write(',\n')
                except Exception as e:
                    spider.logger.error(f"Error writing JSON file {file_path}: {e}")

        return item '''