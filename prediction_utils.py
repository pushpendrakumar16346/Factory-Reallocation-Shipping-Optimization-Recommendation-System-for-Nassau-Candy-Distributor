
from pathlib import Path
import json
import joblib
import pandas as pd


def load_model(model_path):
    """Load a saved joblib model."""
    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    return joblib.load(model_path)


def load_feature_schema(schema_path):
    """Load the saved model feature schema."""
    schema_path = Path(schema_path)

    if not schema_path.exists():
        raise FileNotFoundError(f"Feature schema not found: {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)

    features = schema.get("predictor_features", [])

    if not features:
        raise ValueError("Feature schema contains no predictor features.")

    return features


def validate_prediction_data(data, feature_names):
    """Validate required model input columns without inventing values."""
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Prediction input must be a pandas DataFrame.")

    missing = [col for col in feature_names if col not in data.columns]

    if missing:
        raise ValueError(f"Missing model features: {missing}")

    if data.empty:
        raise ValueError("Prediction input is empty.")

    return data.loc[:, feature_names].copy()


def predict_lead_time(model, data, feature_names):
    """Return model predictions in days; interpretation depends on target definition."""
    X = validate_prediction_data(data, feature_names)
    predictions = model.predict(X)

    return pd.Series(
        predictions,
        index=data.index,
        name="Predicted_Lead_Time_Days"
    )
