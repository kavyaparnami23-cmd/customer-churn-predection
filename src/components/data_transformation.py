import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.logger import logger
from src.exception import CustomException
from src.utils import save_object
from src.config import DataTransformationConfig, DataIngestionConfig

class DataTransformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()
        self.ingestion_config=DataIngestionConfig()

    def get_preprocessor(self):
        numerical_columns=["Tenure Months","Monthly Charges","Total Charges"]
        categorical_columns=["Gender","Senior Citizen","Partner","Dependents","Phone Service","Multiple Lines","Internet Service","Online Security","Online Backup","Device Protection","Tech Support","Streaming TV","Streaming Movies","Contract","Paperless Billing","Payment Method"]
        num_pipeline=Pipeline([("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())])
        cat_pipeline=Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("encoder",OneHotEncoder(handle_unknown="ignore"))])
        return ColumnTransformer([("num",num_pipeline,numerical_columns),("cat",cat_pipeline,categorical_columns)])

    def initiate_data_transformation(self):
        try:
            train_df=pd.read_csv(self.ingestion_config.train_data_path)
            test_df=pd.read_csv(self.ingestion_config.test_data_path)
            train_df["Total Charges"]=pd.to_numeric(train_df["Total Charges"],errors="coerce")
            test_df["Total Charges"]=pd.to_numeric(test_df["Total Charges"],errors="coerce")
            target="Churn Label"
            drop_cols=["CustomerID","Count","Country","State","City","Zip Code","Lat Long","Latitude","Longitude","Churn Value","Churn Score","Churn Reason"]
            drop_cols=[c for c in drop_cols if c in train_df.columns]
            X_train=train_df.drop(columns=drop_cols+[target])
            y_train=train_df[target].map({"Yes":1,"No":0})
            X_test=test_df.drop(columns=drop_cols+[target])
            y_test=test_df[target].map({"Yes":1,"No":0})
            pre=self.get_preprocessor()
            X_train=pre.fit_transform(X_train)
            X_test=pre.transform(X_test)
            train_arr=np.c_[X_train,y_train]
            test_arr=np.c_[X_test,y_test]
            save_object(self.transformation_config.preprocessor_obj_file_path,pre)
            logger.info("Transformation completed")
            return train_arr,test_arr,self.transformation_config.preprocessor_obj_file_path
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataTransformation()
    train_arr,test_arr,path=obj.initiate_data_transformation()
    print(train_arr.shape)
    print(test_arr.shape)
    print(path)
