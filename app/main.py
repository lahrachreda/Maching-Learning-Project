from fastapi import FastAPI
import pandas as pd
from src.predict import predictor
from app.schemas import Transaction

from src.predict import predictor
from fastapi import Header, HTTPException, Depends

API_KEY = "api-fraud-detection"

def verify_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé invalide")

app = FastAPI(
    title="API de détection de fraude bancaire",
    description="Reçoit une transaction et retourne une probabilité de fraude + décision.",
    version="1.0.0"
)
@app.get("/health")
def health():
    return{"status":"ok"}

@app.post("/predict", dependencies=[Depends(verify_key)])
def predict(transaction: Transaction):
    # Convert the transaction to a DataFrame
    transaction_df = pd.DataFrame([transaction.model_dump()])

    # Use the predictor function from predict.py
    result = predictor(transaction_df)

    return result