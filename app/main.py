from fastapi import FastAPI
from app.routers import router

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    description="Predict whether a customer will churn."
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is Running"
    }