from fastapi import APIRouter

from app.schemas import CustomerRequest
from app.services import PredictionService

router = APIRouter()


@router.post("/predict")
def predict(customer: CustomerRequest):

    result = PredictionService.predict(customer)

    return result