from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router

app = FastAPI(

    title="Customer Churn Prediction API",

    description="Predict whether a customer is likely to churn.",

    version="1.0.0"

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {

        "message": "Customer Churn Prediction API is Running"

    }


app.include_router(router)