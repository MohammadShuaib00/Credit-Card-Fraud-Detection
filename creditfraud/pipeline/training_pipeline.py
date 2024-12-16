import os
import sys
from creditfraud.components.data_ingestion import DataIngestion
from creditfraud.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from creditfraud.entity.artifact_entity import DataIngestionArtifact
from creditfraud.logger.logging import logging
from creditfraud.exception.exception import CreditFraudDetection


class TrainingPipeline:
    def __init__(self):
        try:
            logging.info("Initializing the Training Pipeline.")
            self.training_pipeline_config = TrainingPipelineConfig()
            self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            logging.info("Training Pipeline and Data Ingestion configurations initialized successfully.")
        except Exception as e:
            raise CreditFraudDetection(e, sys)

    def start_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process.")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion step completed successfully.")
            return data_ingestion_artifact
        except Exception as a:
            logging.error("Error during data ingestion.", exc_info=True)
            raise CreditFraudDetection(a, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise CreditFraudDetection(e, sys)
        
