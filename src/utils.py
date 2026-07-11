"""
utils.py

Utility functions for saving and loading objects.
"""

import os
import sys
import pickle

from src.exception import CustomException
from src.logger import logger


def save_object(file_path, obj):
    """
    Save Python object using pickle
    """

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logger.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load Python object using pickle
    """

    try:

        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)

        logger.info(f"Object loaded successfully from {file_path}")

        return obj

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":

    sample_data = {
        "Project": "Customer Churn Prediction",
        "Model": "AdaBoost"
    }

    save_object("artifacts/sample.pkl", sample_data)

    loaded_data = load_object("artifacts/sample.pkl")

    print("Loaded Object:")
    print(loaded_data)