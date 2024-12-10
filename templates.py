import os
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

while True:
    project_name = input("Enter the source project name: ")
    if project_name != '':
        break

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logging.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/model/__init__.py",
    f"{project_name}/utils/model/estimator.py",
    f"{project_name}/utils/metric/__init__.py",
    f"{project_name}/utils/metric/get_classification_metric.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    "notebooks/experiment.ipynb",
    "templates/index.html",
    "static/style.css",
    "requirements.txt",
    "setup.py",
    "app.py",
    "test.py",
    "push_data_into_database.py",
    "Dockerfile"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        try:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created: {filedir}")
        except Exception as e:
            logging.error(f"Failed to create directory {filedir}: {e}")
    
    if not filepath.exists() or filepath.stat().st_size == 0:
        try:
            with open(filepath, "w") as file:
                pass
            logging.info(f"File created: {filepath}")
        except Exception as e:
            logging.error(f"Failed to create file {filepath}: {e}")
    else:
        logging.info(f"File already exists: {filepath}")
