import os
import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object
from src.config import PredictionPipelineConfig


class PredictionPipeline:

    def __init__(self):
        self.config = PredictionPipelineConfig()

    def predict(self, features):

        try:

            model = load_object(self.config.model_file_path)

            preprocessor = load_object(
                self.config.preprocessor_file_path
            )

            data_scaled = preprocessor.transform(features)

            prediction = model.predict(data_scaled)

            probability = model.predict_proba(data_scaled)

            return prediction, probability

        except Exception as e:
            raise CustomException(e, sys)


class CustomerData:

    def __init__(
        self,
        Gender,
        Senior_Citizen,
        Partner,
        Dependents,
        Tenure_Months,
        Phone_Service,
        Multiple_Lines,
        Internet_Service,
        Online_Security,
        Online_Backup,
        Device_Protection,
        Tech_Support,
        Streaming_TV,
        Streaming_Movies,
        Contract,
        Paperless_Billing,
        Payment_Method,
        Monthly_Charges,
        Total_Charges
    ):

        self.Gender = Gender
        self.Senior_Citizen = Senior_Citizen
        self.Partner = Partner
        self.Dependents = Dependents
        self.Tenure_Months = Tenure_Months
        self.Phone_Service = Phone_Service
        self.Multiple_Lines = Multiple_Lines
        self.Internet_Service = Internet_Service
        self.Online_Security = Online_Security
        self.Online_Backup = Online_Backup
        self.Device_Protection = Device_Protection
        self.Tech_Support = Tech_Support
        self.Streaming_TV = Streaming_TV
        self.Streaming_Movies = Streaming_Movies
        self.Contract = Contract
        self.Paperless_Billing = Paperless_Billing
        self.Payment_Method = Payment_Method
        self.Monthly_Charges = Monthly_Charges
        self.Total_Charges = Total_Charges

    def get_data_as_dataframe(self):

        data = {

            "Gender":[self.Gender],
            "Senior Citizen":[self.Senior_Citizen],
            "Partner":[self.Partner],
            "Dependents":[self.Dependents],
            "Tenure Months":[self.Tenure_Months],
            "Phone Service":[self.Phone_Service],
            "Multiple Lines":[self.Multiple_Lines],
            "Internet Service":[self.Internet_Service],
            "Online Security":[self.Online_Security],
            "Online Backup":[self.Online_Backup],
            "Device Protection":[self.Device_Protection],
            "Tech Support":[self.Tech_Support],
            "Streaming TV":[self.Streaming_TV],
            "Streaming Movies":[self.Streaming_Movies],
            "Contract":[self.Contract],
            "Paperless Billing":[self.Paperless_Billing],
            "Payment Method":[self.Payment_Method],
            "Monthly Charges":[self.Monthly_Charges],
            "Total Charges":[self.Total_Charges]
        }

        return pd.DataFrame(data)


if __name__ == "__main__":

    customer = CustomerData(

        Gender="Male",
        Senior_Citizen="No",
        Partner="Yes",
        Dependents="No",
        Tenure_Months=12,
        Phone_Service="Yes",
        Multiple_Lines="No",
        Internet_Service="Fiber Optic",
        Online_Security="No",
        Online_Backup="Yes",
        Device_Protection="Yes",
        Tech_Support="No",
        Streaming_TV="Yes",
        Streaming_Movies="Yes",
        Contract="Month-to-month",
        Paperless_Billing="Yes",
        Payment_Method="Electronic check",
        Monthly_Charges=75.25,
        Total_Charges=903.00

    )

    df = customer.get_data_as_dataframe()

    pipeline = PredictionPipeline()

    prediction, probability = pipeline.predict(df)

    print("=" * 50)
    print("Prediction :", prediction[0])
    print("Probability :", probability[0])
    print("=" * 50)