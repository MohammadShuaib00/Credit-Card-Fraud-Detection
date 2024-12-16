import os
import sys
import pymongo
import json
import certifi
import pandas as pd
from dotenv import load_dotenv
from creditfraud.exception.exception import CreditFraudDetection
from creditfraud.logger.logging import logging
from creditfraud.constants import training

# Load environment variables from a .env file
load_dotenv()

# Get the MongoDB URL from the environment variables
MONGODB_URL = os.getenv("MONGO_DB_URL")

# Get the CA certificates for a secure connection
ca = certifi.where()


class CreditDataExtract:
    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def cv_to_json_convert(self, file_path):
        try:
            logging.info("Data is being converted into JSON format")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            logging.info("Data converted successfully.")
            return records
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def insert_data_mongodb(self, records):
        try:
            database_name = training.DATABASE_NAME
            collection_name = training.COLLECTION_NAME

            # Connect to the database and collection
            database = self.mongo_client[database_name]
            collection = database[collection_name]

            # Insert the records into the collection
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise CreditFraudDetection(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Data/creditcard.csv"
    creditObj = CreditDataExtract()
    
    # Convert the CSV data to JSON records
    records = creditObj.cv_to_json_convert(file_path=FILE_PATH)
    no_of_records = creditObj.insert_data_mongodb(records=records)
    print("Number of inserted rows:", no_of_records)
