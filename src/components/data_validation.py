"""
data_validation.py

Author : Kavya Parnami
Project : Customer Churn Prediction

Responsibilities:
1. Read train and test datasets
2. Validate dataset
3. Check required columns
4. Check missing values
5. Check duplicate rows
6. Generate validation report
"""

import os
import sys
import yaml
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.config import (
    DataValidationConfig,
    DataIngestionConfig
)


class DataValidation:

    def __init__(self):

        self.validation_config = DataValidationConfig()

        self.ingestion_config = DataIngestionConfig()

    def validate_dataset(self):

        logger.info("=" * 70)
        logger.info("DATA VALIDATION STARTED")

        try:

            train_df = pd.read_csv(
                self.ingestion_config.train_data_path
            )

            test_df = pd.read_csv(
                self.ingestion_config.test_data_path
            )

            logger.info("Train and Test datasets loaded successfully.")

            required_columns = [

                "Gender",
                "Senior Citizen",
                "Partner",
                "Dependents",
                "Tenure Months",
                "Phone Service",
                "Multiple Lines",
                "Internet Service",
                "Online Security",
                "Online Backup",
                "Device Protection",
                "Tech Support",
                "Streaming TV",
                "Streaming Movies",
                "Contract",
                "Paperless Billing",
                "Payment Method",
                "Monthly Charges",
                "Total Charges",
                "Churn Label"

            ]

            validation_report = {}

            # -------------------------------------------------
            # Dataset Exists
            # -------------------------------------------------

            validation_report["train_dataset_exists"] = os.path.exists(
                self.ingestion_config.train_data_path
            )

            validation_report["test_dataset_exists"] = os.path.exists(
                self.ingestion_config.test_data_path
            )

            # -------------------------------------------------
            # Required Columns
            # -------------------------------------------------

            missing_columns = [
                col for col in required_columns
                if col not in train_df.columns
            ]

            validation_report["missing_columns"] = missing_columns

            validation_report["required_columns_present"] = (
                len(missing_columns) == 0
            )

            # -------------------------------------------------
            # Missing Values
            # -------------------------------------------------

            validation_report["missing_values_train"] = int(
                train_df.isnull().sum().sum()
            )

            validation_report["missing_values_test"] = int(
                test_df.isnull().sum().sum()
            )

            # -------------------------------------------------
            # Duplicate Rows
            # -------------------------------------------------

            validation_report["duplicate_rows_train"] = int(
                train_df.duplicated().sum()
            )

            validation_report["duplicate_rows_test"] = int(
                test_df.duplicated().sum()
            )

            # -------------------------------------------------
            # Empty Dataset
            # -------------------------------------------------

            validation_report["train_empty"] = train_df.empty

            validation_report["test_empty"] = test_df.empty

            # -------------------------------------------------
            # Final Status
            # -------------------------------------------------

            validation_report["status"] = (
                "PASS"
                if validation_report["required_columns_present"]
                else "FAIL"
            )

            os.makedirs("artifacts", exist_ok=True)

            with open(
                self.validation_config.validation_report_file_path,
                "w"
            ) as file:

                yaml.dump(
                    validation_report,
                    file,
                    default_flow_style=False
                )

            logger.info("Validation Report Generated Successfully")

            logger.info("DATA VALIDATION COMPLETED")

            logger.info("=" * 70)

            return validation_report

        except Exception as e:

            logger.error("Error During Data Validation")

            raise CustomException(e, sys)


if __name__ == "__main__":

    validation = DataValidation()

    report = validation.validate_dataset()

    print("\nValidation Report\n")

    print(report)