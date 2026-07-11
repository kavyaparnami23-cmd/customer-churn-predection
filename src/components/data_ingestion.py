"""
data_ingestion.py

Author : Kavya Parnami
Project : Customer Churn Prediction

Responsibilities:
1. Read raw dataset
2. Save raw dataset in artifacts
3. Split into train and test
4. Save train.csv and test.csv
"""

import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException
from src.config import DataIngestionConfig


class DataIngestion:
    """
    Handles data ingestion process.
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the dataset, stores a raw copy,
        splits into train and test sets,
        and saves them inside the artifacts folder.
        """

        logger.info("=" * 70)
        logger.info("Data Ingestion Started")

        try:

            logger.info("Reading dataset...")

            df = pd.read_csv(
                self.ingestion_config.dataset_path
            )

            logger.info(f"Dataset Loaded Successfully")
            logger.info(f"Dataset Shape : {df.shape}")

            #####################################################
            # Create Artifacts Folder
            #####################################################

            os.makedirs(
                os.path.dirname(self.ingestion_config.raw_data_path),
                exist_ok=True
            )

            #####################################################
            # Save Raw Dataset
            #####################################################

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logger.info("Raw Dataset Saved Successfully")

            #####################################################
            # Train Test Split
            #####################################################

            logger.info("Performing Train-Test Split")

            train_set, test_set = train_test_split(
                df,
                test_size=0.20,
                random_state=42,
                stratify=df["Churn Label"]      # Keeps churn ratio balanced
            )

            #####################################################
            # Save Train Dataset
            #####################################################

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            logger.info("Train Dataset Saved Successfully")

            #####################################################
            # Save Test Dataset
            #####################################################

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logger.info("Test Dataset Saved Successfully")

            logger.info("Data Ingestion Completed Successfully")
            logger.info("=" * 70)

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            logger.error("Exception Occurred During Data Ingestion")

            raise CustomException(e, sys)


if __name__ == "__main__":

    ingestion = DataIngestion()

    train_path, test_path = ingestion.initiate_data_ingestion()

    print("\nTrain File :", train_path)

    print("Test File  :", test_path)