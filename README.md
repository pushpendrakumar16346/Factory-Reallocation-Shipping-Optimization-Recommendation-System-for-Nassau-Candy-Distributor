# Nassau Candy Distributor Analytics Project

## Overview

This project analyses historical Nassau Candy Distributor data
using data cleaning, exploratory data analysis, feature engineering,
predictive modelling, clustering, factory-reference analysis,
scenario simulation and decision-support methods.

An interactive Streamlit dashboard is included.

## Project Structure

- data/raw: original input data
- data/processed: processed data and application bundle
- notebooks: analytical Jupyter notebooks
- reports: analytical reports and final delivery documents

## Environment Setup

Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Install dependencies:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

## Run the Dashboard

    cd data/processed/app_bundle
    streamlit run app.py

Open the local URL shown in the terminal.

## Dashboard Pages

- Home
- Product Performance
- Region Analysis
- Ship Mode Analysis
- Factory Explorer
- Scenario Simulator
- Recommendations
- Risk and Impact

## Data

The original dataset is expected at:

    data/raw/Nassau Candy Distributor.csv

Keep the original raw dataset unchanged.

## Important Limitations

- Lead time is Ship Date minus Order Date.
- It is not independently verified carrier transit time.
- Factory mappings are reference mappings.
- Straight-line distance is not freight route distance.
- Factory-specific savings have not been established.
- Scenario support is not a probability of success.
- Model evaluation outputs contain unresolved discrepancies.

Review the executive summary and model validation report
before using results for management decisions.