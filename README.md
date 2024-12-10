### Credit Card Fraud Detection Predictive Models

## Introduction

The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred over two days, with 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, with the positive class (frauds) accounting for only 0.172% of all transactions.

### Features:
- **V1, V2, ... V28**: These are the principal components obtained through PCA transformation.
- **Time**: Represents the seconds elapsed from the first transaction.
- **Amount**: The transaction amount. This feature can be particularly useful for example-dependent cost-sensitive learning.
- **Class**: The response variable that takes the value 1 in the case of fraud and 0 for non-fraudulent transactions.

Due to confidentiality issues, the original features and additional background information about the data are not provided.

## Pipeline Flow

The credit card fraud detection model follows a structured pipeline comprising several components, each responsible for a specific task in the data processing and model training workflow. The pipeline consists of the following components organized within the `components` folder:

### 1. **Data Ingestion**:
   - **`data_ingestion.py`**: This component handles the ingestion of the dataset, which includes loading the transactions data from its source into a suitable format for further processing. It deals with reading the raw data files and performing initial data validation.

### 2. **Data Validation**:
   - **`data_validation.py`**: After ingestion, the data undergoes validation to check for missing values, outliers, and other data quality issues. This component ensures that the data meets the necessary criteria for training the model.

### 3. **Data Transformation**:
   - **`data_transformation.py`**: This step involves applying necessary transformations to the data, such as scaling features using PCA (Principal Component Analysis). It prepares the data for model training by transforming the features into a reduced dimension while retaining the important information.

### 4. **Model Training**:
   - **`model_trainer.py`**: This component is responsible for training the machine learning model. It takes the processed data and trains a classifier to predict fraud. It might involve multiple models and hyperparameter tuning for selecting the best model.

### 5. **Model Evaluation**:
   - **`model_evaluation.py`**: After training, the model's performance is evaluated using various metrics such as accuracy, precision, recall, and F1 score. This component ensures that the model meets the desired performance criteria before deployment.

### 6. **Prediction Pipeline**:
   - **`prediction_pipeline.py`**: This component handles the application of the trained model to new data for making predictions about fraud. It is responsible for the inference process and prepares the results for reporting or further analysis.

### 7. **Logging**:
   - **`logging.py`**: Logs are generated throughout the pipeline to track the progress and any issues that might occur during the process. This component ensures proper logging for debugging and monitoring purposes.

### 8. **Exception Handling**:
   - **`exception/exception.py`**: Manages exceptions and errors that might occur during the pipeline's execution. It allows graceful handling of errors and helps maintain the pipeline’s stability and reliability.

### 9. **Utilities**:
   - **`utils/model/estimator.py`**: Contains helper functions for model operations, such as model serialization and deserialization, feature selection, and other utility functions that support the components throughout the pipeline.
   - **`utils/metric/get_classification_metric.py`**: Computes performance metrics for classification models, which is crucial for evaluating model predictions and guiding model improvements.
   - **`constants/training.py`**: Defines constants used throughout the pipeline, including file paths, column names, and model hyperparameters.

Each component is designed to operate independently, facilitating modularity and ease of integration with other parts of the project. The pipeline flow ensures that the data goes through a series of steps, from ingestion to prediction, with each step building upon the previous one to produce a reliable fraud detection model.

