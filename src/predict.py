import joblib
import pandas as pd
from pathlib import Path
import logging
logger = logging.getLogger(__name__)
THRESHOLD = 0.15

BASE_DIR = Path(__file__).resolve().parent.parent

preprocessor = joblib.load(
    BASE_DIR / "models" / "preprocessor.pkl"
)

model = joblib.load(
    BASE_DIR / "models" / "model_LR.pkl"
)

label_encoder = joblib.load(
    BASE_DIR / "models" / "label_encoder.pkl"
)

def predictor(transaction: pd.DataFrame):

    # Use the already-fitted preprocessor
    data_encoded = preprocessor.transform(transaction)

    # Prediction
    prediction_encoded = model.predict(data_encoded)[0]

    # Probability
    probability = model.predict_proba(data_encoded)[0, 1]

    # Decode label
    prediction = label_encoder.inverse_transform(
        [prediction_encoded]
    )[0]
    decision = "BLOCK" if probability >= THRESHOLD else "ALLOW"
    logger.info(f"probability={probability:.4f} decision={decision}")

    return {
        "fraud_probability": probability,
         "decision": decision
         }

   