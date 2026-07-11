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

            logger.info("Splitting train and test arrays")

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info("Training AdaBoost Model")

            model = AdaBoostClassifier(
                learning_rate=1,
                n_estimators=100,
                random_state=42
            )

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, y_prob)

            print("=" * 50)
            print("Model Evaluation")
            print("=" * 50)
            print(f"Accuracy  : {accuracy:.4f}")
            print(f"Precision : {precision:.4f}")
            print(f"Recall    : {recall:.4f}")
            print(f"F1 Score  : {f1:.4f}")
            print(f"ROC AUC   : {roc_auc:.4f}")

            logger.info("Saving trained model")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logger.info("Model saved successfully")

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":

    from src.components.data_transformation import DataTransformation

    transformer = DataTransformation()

    train_arr, test_arr, _ = transformer.initiate_data_transformation()

    trainer = ModelTrainer()

    trainer.initiate_model_trainer(
        train_arr,
        test_arr
    )