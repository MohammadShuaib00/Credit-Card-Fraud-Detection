from datetime import datetime
import logging
import os,sys

# Generate the unique log file name
LOG_FILE_PATH = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the log directory
DIR_PATH_NAME = os.path.join(os.getcwd(),"logs")

# Make the directory
os.makedirs(DIR_PATH_NAME,exist_ok=True)


# Combining the dir and log file path
FULL_LOG_FILE_PATH = os.path.join(DIR_PATH_NAME,LOG_FILE_PATH)

#Define configuration for the logs
logging.basicConfig(
    filename=FULL_LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - %(module)s - Line: %(lineno)d",
)