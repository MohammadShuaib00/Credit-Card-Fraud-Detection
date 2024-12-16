import os,sys
import numpy as np
import pandas as pd
from creditfraud.logger.logging import logging
from creditfraud.exception.exception import CreditFraudDetection
from creditfraud.constants import training
from datetime import datetime


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        try:
            timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
            self.artifact_name = training.ARTIFACT_DIR
            self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        except Exception as e:
            raise CreditFraudDetection(e,sys)

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir,training.DATA_INGESTION_DIR_NAME)
            self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir,training.DATA_INGESTION_RAW_DIR,training.RAW_FILE_PATH)
            self.train_file_path:str = os.path.join(self.data_ingestion_dir,training.DATA_INGESTED_DIR,training.TRAIN_FILE_PATH)
            self.test_file_path:str  = os.path.join(self.data_ingestion_dir,training.DATA_INGESTED_DIR,training.TEST_FILE_PATH)
            self.split_ration:float = training.SPLIT_RATION
            self.random_state:int = training.RANDOM_STATE
            self.database_name:str = training.DATABASE_NAME
            self.collection_name:str = training.COLLECTION_NAME
        except Exception as e:
            raise CreditFraudDetection(e,sys)

