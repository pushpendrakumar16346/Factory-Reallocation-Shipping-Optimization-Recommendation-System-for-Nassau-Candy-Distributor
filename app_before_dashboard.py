from pathlib import Path
import sys
import json
import joblib
import pandas as pd
import streamlit as st

# Configure application paths
APP_ROOT = Path(__file__).resolve().parent

DATA_DIR = APP_ROOT / "data"
MODEL_DIR = APP_ROOT / "models"
REPORT_DIR = APP_ROOT / "reports"
SRC_DIR = APP_ROOT / "src"

for directory in [DATA_DIR, MODEL_DIR, REPORT_DIR, SRC_DIR]:
    if not directory.exists():
        raise FileNotFoundError(f"Required application directory not found: {directory}")

if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

# Page configuration
st.set_page_config(
    page_title="Nassau Candy Analytics",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application title
st.title("Nassau Candy Distribution Analytics")
st.caption(
    "Business performance, derived lead-time analysis, "
    "product priorities and factory reference exploration"
)

# Load application datasets
@st.cache_data
def load_csv(file_path):
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Required CSV file not found: {path}")
    return pd.read_csv(path, low_memory=False)

# Load machine learning model
@st.cache_resource
def load_lead_time_model():
    model_path = MODEL_DIR / "Nassau_Lead_Time_Model.joblib"
    if not model_path.is_file():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return joblib.load(model_path)

# Load model metadata
@st.cache_data
def load_model_metadata():
    metadata_path = MODEL_DIR / "model_metadata.json"
    if not metadata_path.is_file():
        raise FileNotFoundError(f"Model metadata not found: {metadata_path}")
    with open(metadata_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Load feature schema
@st.cache_data
def load_feature_schema():
    schema_path = MODEL_DIR / "feature_schema.json"
    if not schema_path.is_file():
        raise FileNotFoundError(f"Feature schema not found: {schema_path}")
    with open(schema_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Load existing application modules
try:
    from src.prediction_utils import (
        load_model,
        load_feature_schema as load_predictor_feature_schema,
        predict_lead_time
    )
    from src.feature_utils import prepare_model_features
    from src.scenario_utils import review_factory_options
    from src.recommendation_utils import (
        rank_existing_priorities,
        get_factory_option_warnings
    )
    MODULES_AVAILABLE = True
    MODULE_ERROR = None

except Exception as error:
    MODULES_AVAILABLE = False
    MODULE_ERROR = str(error)

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Home",
        "Product Performance",
        "Region Analysis",
        "Ship Mode Analysis",
        "Factory Explorer",
        "Scenario Simulator",
        "Recommendations",
        "Risk and Impact"
    ]
)

# Application data loader
REQUIRED_FILES = {
    "processed_data": DATA_DIR / "processed_dataset.csv",
    "factory_master": DATA_DIR / "factory_master.csv",
    "product_mapping": DATA_DIR / "product_factory_mapping.csv",
    "kpi_dashboard": DATA_DIR / "kpis" / "kpi_dashboard_data.csv",
    "risk_register": DATA_DIR / "kpis" / "risk_register.csv",
    "recommendations": REPORT_DIR / "recommendations" / "ranked_product_recommendations.csv",
    "factory_options": REPORT_DIR / "recommendations" / "Phase_10_Factory_Option_Screening.csv",
    "region_risk": DATA_DIR / "kpis" / "region_performance_risk.csv",
    "model_metrics": REPORT_DIR / "model_metrics" / "ML_Final_Model_Comparison.csv"
}

@st.cache_data
def load_application_data():
    loaded = {}
    errors = []

    for key, path in REQUIRED_FILES.items():
        try:
            loaded[key] = load_csv(path)
        except Exception as error:
            errors.append(f"{key}: {error}")

    return loaded, errors

try:
    APP_DATA, DATA_ERRORS = load_application_data()
except Exception as error:
    APP_DATA = {}
    DATA_ERRORS = [str(error)]

# Load model resources
try:
    MODEL = load_lead_time_model()
    MODEL_METADATA = load_model_metadata()
    FEATURE_SCHEMA = load_feature_schema()
    MODEL_AVAILABLE = True
    MODEL_ERROR = None

except Exception as error:
    MODEL = None
    MODEL_METADATA = {}
    FEATURE_SCHEMA = {}
    MODEL_AVAILABLE = False
    MODEL_ERROR = str(error)

# Global application status
if not MODULES_AVAILABLE:
    st.sidebar.warning("Some application modules could not be imported.")

if DATA_ERRORS:
    with st.expander("Data loading warnings", expanded=True):
        for error in DATA_ERRORS:
            st.warning(error)

# Home page foundation
if page == "Home":
    st.header("Dashboard Overview")

    st.write(
        "Welcome to the Nassau Candy analytics application. "
        "Use the sidebar to explore business performance, "
        "product priorities, regional patterns and scenario evidence."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if "processed_data" in APP_DATA:
            st.metric(
                "Dataset Records",
                f"{len(APP_DATA['processed_data']):,}"
            )
        else:
            st.metric("Dataset Records", "Unavailable")

    with col2:
        st.metric(
            "Model Status",
            "Available" if MODEL_AVAILABLE else "Unavailable"
        )

    with col3:
        st.metric(
            "Module Status",
            "Available" if MODULES_AVAILABLE else "Review Required"
        )

    st.info(
        "Lead-time values represent derived date differences, "
        "not independently verified physical transit times."
    )

# Other pages: implementation foundation
else:
    st.header(page)
    st.info(
        "This page is part of the application navigation foundation. "
        "Its analytical components will be added in the corresponding "
        "dashboard implementation tasks."
    )

# Footer
st.divider()
st.caption(
    "Nassau Candy Analytics | Exploratory decision support | "
    "Factory mappings are reference mappings, not verified dispatch records."
)
