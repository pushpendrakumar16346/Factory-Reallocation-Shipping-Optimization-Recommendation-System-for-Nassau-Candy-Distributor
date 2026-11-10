
import numpy as np
import pandas as pd


def add_order_date_features(data, date_column="Order Date"):
    """
    Add date features used by the saved model.
    Original date column is preserved.
    """
    if date_column not in data.columns:
        raise ValueError(f"Missing date column: {date_column}")

    result = data.copy()

    parsed_dates = pd.to_datetime(
        result[date_column],
        dayfirst=True,
        errors="coerce"
    )

    if parsed_dates.isna().any():
        raise ValueError(
            "Some order dates could not be parsed. "
            "Review source date values before prediction."
        )

    result["Order_Year"] = parsed_dates.dt.year
    result["Order_Month"] = parsed_dates.dt.month
    result["Order_Quarter"] = parsed_dates.dt.quarter
    result["Order_Weekday"] = parsed_dates.dt.day_name()

    return result


def safe_divide(numerator, denominator):
    """Divide safely; zero denominators produce NaN."""
    numerator = pd.to_numeric(numerator, errors="coerce")
    denominator = pd.to_numeric(denominator, errors="coerce")

    result = numerator.div(denominator.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def add_financial_features(data):
    """
    Add financial ratio features using the source dataset's
    Sales, Cost, Gross Profit and Units fields.

    Profit_Margin_Pct is expressed as a percentage.
    """
    required = ["Sales", "Cost", "Gross Profit", "Units"]
    missing = [col for col in required if col not in data.columns]

    if missing:
        raise ValueError(f"Missing financial columns: {missing}")

    result = data.copy()

    result["Profit_Margin_Pct"] = (
        safe_divide(result["Gross Profit"], result["Sales"]) * 100
    )

    result["Sales_Per_Unit"] = safe_divide(
        result["Sales"], result["Units"]
    )

    result["Cost_Per_Unit"] = safe_divide(
        result["Cost"], result["Units"]
    )

    result["Profit_Per_Unit"] = safe_divide(
        result["Gross Profit"], result["Units"]
    )

    return result


def prepare_model_features(data):
    """
    Apply date and financial transformations.
    Does not remove rows or overwrite original source columns.
    """
    result = add_order_date_features(data)
    result = add_financial_features(result)
    return result
