import pandas as pd

from src.pipeline.prediction_pipeline import PredictionPipeline


class PredictionService:

    @staticmethod
    def predict(customer):

        data = pd.DataFrame({

            "Gender": [customer.Gender],
            "Senior Citizen": [customer.Senior_Citizen],
            "Partner": [customer.Partner],
            "Dependents": [customer.Dependents],
            "Tenure Months": [customer.Tenure_Months],
            "Phone Service": [customer.Phone_Service],
            "Multiple Lines": [customer.Multiple_Lines],
            "Internet Service": [customer.Internet_Service],
            "Online Security": [customer.Online_Security],
            "Online Backup": [customer.Online_Backup],
            "Device Protection": [customer.Device_Protection],
            "Tech Support": [customer.Tech_Support],
            "Streaming TV": [customer.Streaming_TV],
            "Streaming Movies": [customer.Streaming_Movies],
            "Contract": [customer.Contract],
            "Paperless Billing": [customer.Paperless_Billing],
            "Payment Method": [customer.Payment_Method],
            "Monthly Charges": [customer.Monthly_Charges],
            "Total Charges": [customer.Total_Charges]

        })

        pipeline = PredictionPipeline()

        prediction, probability = pipeline.predict(data)

        prediction = int(prediction[0])

        return {

            "prediction": "Churn" if prediction == 1 else "No Churn",

            "prediction_code": prediction,

            "probability_no_churn": f"{probability[0][0]*100:.2f}%",

            "probability_churn": f"{probability[0][1]*100:.2f}%"

        }