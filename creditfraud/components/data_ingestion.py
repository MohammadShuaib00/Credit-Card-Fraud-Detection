import os
import sys
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from creditfraud.entity.config_entity import DataIngestionConfig
# from creditfraud.entity.artifact_entity import DataIngestionArtifact
from creditfraud.logger.logging import logging
from creditfraud.exception.exception import CreditFraudDetection
import pymongo
from creditfraud.entity.artifact_entity import DataIngestionArtifact

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info("Initializing Data Ingestion configuration.")
            if not MONGO_DB_URL:
                raise ValueError("MongoDB URL is not found in environment variables.")
            self.data_ingestion_config = data_ingestion_config
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            os.makedirs(self.data_ingestion_config.data_ingestion_dir, exist_ok=True)
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            logging.info("Exporting data from MongoDB collection to DataFrame.")
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            # Fetch records from MongoDB
            collection = self.mongo_client[database_name][collection_name]
            records = list(collection.find())

            if not records:
                logging.info("MongoDB collection is empty. Returning an empty DataFrame.")
                return pd.DataFrame()

            data = pd.DataFrame(records)

            # Drop '_id' column if present
            if "_id" in data.columns:
                data.drop(columns=["_id"], inplace=True)
                logging.info("Dropped '_id' column from the DataFrame.")

            # Replace 'na' strings with NaN
            data.replace({"na": np.nan}, inplace=True)
            logging.info(f"Successfully exported {len(data)} records to DataFrame.")
            return data
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame) -> None:
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Data successfully saved to feature store at: {feature_store_file_path}")
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def split_data_into_train_test_file(self, dataframe: pd.DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.split_ration
            )
            logging.info("Performed train-test split.")

            train_file_path = self.data_ingestion_config.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path

            os.makedirs(os.path.dirname(train_file_path), exist_ok=True)

            train_set.to_csv(train_file_path, index=False, header=True)
            test_set.to_csv(test_file_path, index=False, header=True)

            logging.info(f"Train data saved to: {train_file_path}")
            logging.info(f"Test data saved to: {test_file_path}")
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion process.")
            dataframe = self.export_collection_as_dataframe()

            self.export_data_into_feature_store(dataframe)
            self.split_data_into_train_test_file(dataframe)

            data_ingestion_artifact = DataIngestionArtifact(
                raw_data_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path,
            )
            logging.info("Data ingestion process completed.")
            return data_ingestion_artifact
        except Exception as e:
            raise CreditFraudDetection(e, sys)
