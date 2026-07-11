import sys

from src.logger import logger
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainingPipeline:

    def start_training_pipeline(self):

        try:

            logger.info("Training Pipeline Started")

            # Data Ingestion
            ingestion = DataIngestion()
            train_path, test_path = ingestion.initiate_data_ingestion()

            # Data Validation
            validation = DataValidation()
            validation.initiate_data_validation(train_path, test_path)

            # Data Transformation
            transformation = DataTransformation()
            train_arr, test_arr, _ = transformation.initiate_data_transformation()

            # Model Training
            trainer = ModelTrainer()
            accuracy = trainer.initiate_model_trainer(train_arr, test_arr)

            print("=" * 60)
            print("Training Pipeline Completed Successfully")
            print(f"Final Accuracy : {accuracy:.4f}")
            print("=" * 60)

            logger.info("Training Pipeline Completed")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":

    pipeline = TrainingPipeline()
    pipeline.start_training_pipeline()