import os
import sys 

# Common Constants for Training Pipeline
ARTIFACT_DIR: str = "artifacts"
TARGET_COLUMNS: str = "Class" 
TRAIN_FILE_PATH: str = "train.csv" 
TEST_FILE_PATH: str = "test.csv"
RAW_FILE_PATH:str = "data.csv"

# Data Ingestion Related Constants
COLLECTION_NAME: str = "creditfrauddata" 
DATABASE_NAME: str = "data"  
DATA_INGESTION_DIR_NAME: str = "data_ingestion" 
DATA_INGESTION_RAW_DIR: str = "raw" 
DATA_INGESTED_DIR: str = "ingested"
RANDOM_STATE:int = 42
SPLIT_RATION:float = 0.20



