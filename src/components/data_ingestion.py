"""
Data Ingestion Component

Reads the dataset, stores the raw copy,
splits the data into train and test sets,
and saves them in the artifacts folder.
"""

import sys
import pandas as pd

from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException
from src.config import DataIngestionConfig


class DataIngestion:
    """
    Data Ingestion Class
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Read dataset and create train-test split.
        """

        logger.info("Entered Data Ingestion Component")

        try:

            logger.info("Reading dataset")

            df = pd.read_csv(
                self.ingestion_config.dataset_path
            )

            logger.info("Dataset Loaded Successfully")

            import os

            os.makedirs(
                "artifacts",
                exist_ok=True
            )

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logger.info("Raw Dataset Saved")

            logger.info("Performing Train Test Split")

            train_set, test_set = train_test_split(
                df,
                test_size=0.20,
                random_state=42
            )

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logger.info("Train Test Split Completed")

            logger.info("Data Ingestion Completed Successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            logger.error(str(e))

            raise CustomException(e, sys)


if __name__ == "__main__":

    ingestion = DataIngestion()

    train_path, test_path = ingestion.initiate_data_ingestion()

    print(train_path)

    print(test_path)