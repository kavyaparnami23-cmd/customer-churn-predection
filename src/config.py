"""
config.py

Configuration file for the Customer Churn Prediction Project

Author: Kavya Parnami
"""

import os
from dataclasses import dataclass


# ==========================================================
# Artifacts Directory
# ==========================================================

ARTIFACTS_DIR = "artifacts"


# ==========================================================
# Data Ingestion Configuration
# ==========================================================

@dataclass
class DataIngestionConfig:
    """
    Configuration for Data Ingestion
    """

    dataset_path: str = os.path.join(
        "dataset",
        "raw",
        "_customer_churn.csv"
    )

    raw_data_path: str = os.path.join(
        ARTIFACTS_DIR,
        "raw.csv"
    )

    train_data_path: str = os.path.join(
        ARTIFACTS_DIR,
        "train.csv"
    )

    test_data_path: str = os.path.join(
        ARTIFACTS_DIR,
        "test.csv"
    )


# ==========================================================
# Data Validation Configuration
# ==========================================================

@dataclass
class DataValidationConfig:
    """
    Configuration for Data Validation
    """

    validation_report_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "validation_report.yaml"
    )


# ==========================================================
# Data Transformation Configuration
# ==========================================================

@dataclass
class DataTransformationConfig:
    """
    Configuration for Data Transformation
    """

    preprocessor_obj_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "preprocessor.pkl"
    )


# ==========================================================
# Model Trainer Configuration
# ==========================================================

@dataclass
class ModelTrainerConfig:
    """
    Configuration for Model Trainer
    """

    trained_model_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "model.pkl"
    )

    expected_accuracy: float = 0.80

    random_state: int = 42


# ==========================================================
# Model Evaluation Configuration
# ==========================================================

@dataclass
class ModelEvaluationConfig:
    """
    Configuration for Model Evaluation
    """

    metrics_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "metrics.json"
    )


# ==========================================================
# Prediction Pipeline Configuration
# ==========================================================

@dataclass
class PredictionPipelineConfig:
    """
    Configuration for Prediction Pipeline
    """

    model_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "model.pkl"
    )

    preprocessor_file_path: str = os.path.join(
        ARTIFACTS_DIR,
        "preprocessor.pkl"
    )


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    ingestion = DataIngestionConfig()
    validation = DataValidationConfig()
    transformation = DataTransformationConfig()
    trainer = ModelTrainerConfig()

    print("Dataset Path:")
    print(ingestion.dataset_path)

    print("\nRaw Data:")
    print(ingestion.raw_data_path)

    print("\nTrain Data:")
    print(ingestion.train_data_path)

    print("\nTest Data:")
    print(ingestion.test_data_path)

    print("\nPreprocessor Path:")
    print(transformation.preprocessor_obj_file_path)

    print("\nModel Path:")
    print(trainer.trained_model_file_path)