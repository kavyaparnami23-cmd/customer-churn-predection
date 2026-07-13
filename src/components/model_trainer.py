import sys
import numpy as np

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from src.logger import logger
from src.exception import CustomException
from src.utils import save_object
from src.config import ModelTrainerConfig


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):

        try:

            logger.info("=" * 70)
            logger.info("MODEL TRAINING STARTED")
            logger.info("=" * 70)

            # ======================================================
            # Split Train & Test
            # ======================================================

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info(f"Training Samples : {X_train.shape[0]}")
            logger.info(f"Testing Samples  : {X_test.shape[0]}")
            logger.info(f"Number of Features : {X_train.shape[1]}")

            # ======================================================
            # Final Model
            # ======================================================

            logger.info("Training AdaBoost Classifier...")

            model = AdaBoostClassifier(
                learning_rate=1,
                n_estimators=100,
                random_state=42
            )

            model.fit(X_train, y_train)

            logger.info("Model Training Completed")

            # ======================================================
            # Prediction
            # ======================================================

            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]

            # ======================================================
            # Evaluation
            # ======================================================

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, y_prob)

            # ======================================================
            # Console Output
            # ======================================================

            print("\n")
            print("=" * 70)
            print("MODEL EVALUATION")
            print("=" * 70)
            print(f"Model Name : AdaBoostClassifier")
            print(f"Accuracy   : {accuracy:.4f}")
            print(f"Precision  : {precision:.4f}")
            print(f"Recall     : {recall:.4f}")
            print(f"F1 Score   : {f1:.4f}")
            print(f"ROC AUC    : {roc_auc:.4f}")
            print("=" * 70)

            # ======================================================
            # Logging
            # ======================================================

            logger.info("=" * 70)
            logger.info("FINAL MODEL DETAILS")
            logger.info("=" * 70)

            logger.info("Model Name : AdaBoostClassifier")

            logger.info("Hyperparameters :")
            logger.info("learning_rate = 1")
            logger.info("n_estimators = 100")
            logger.info("random_state = 42")

            logger.info("-" * 70)

            logger.info(f"Accuracy  : {accuracy:.4f}")
            logger.info(f"Precision : {precision:.4f}")
            logger.info(f"Recall    : {recall:.4f}")
            logger.info(f"F1 Score  : {f1:.4f}")
            logger.info(f"ROC AUC   : {roc_auc:.4f}")

            # ======================================================
            # Save Model
            # ======================================================

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logger.info("-" * 70)
            logger.info(
                f"Model Saved Successfully at : {self.model_trainer_config.trained_model_file_path}"
            )

            logger.info("=" * 70)
            logger.info("MODEL TRAINING COMPLETED SUCCESSFULLY")
            logger.info("=" * 70)

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":

    from src.components.data_transformation import DataTransformation

    transformation = DataTransformation()

    train_arr, test_arr, _ = transformation.initiate_data_transformation()

    trainer = ModelTrainer()

    trainer.initiate_model_trainer(
        train_arr,
        test_arr
    )