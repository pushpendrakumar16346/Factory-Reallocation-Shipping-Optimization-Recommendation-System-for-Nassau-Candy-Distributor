# Nassau Candy Distributor Dashboard - User Manual

## Starting the Application

1. Open Command Prompt or PowerShell.
2. Navigate to the application folder:

       cd data/processed/app_bundle

3. Start the dashboard:

       streamlit run app.py

4. Open the local browser address displayed by Streamlit.

## Dashboard Pages

### Home
Displays the project overview and summary information.

### Product Performance
Explore product-level sales and performance patterns.

### Region Analysis
Review regional sales and profitability.

### Ship Mode Analysis
Explore shipping-category records and related measures.

### Factory Explorer
Review product-to-factory reference information.
Mappings are not confirmed historical dispatch records.

### Scenario Simulator
Explore supported scenario information.
Scenario support does not establish actual savings,
operational feasibility or probability of success.

### Recommendations
Review indicative analytical priorities.
Recommendations are not proven optimal decisions.

### Risk and Impact
Review risks and analytical limitations.

## Filters and Downloads

Use available filters to narrow the displayed information.
Use CSV or Excel download controls where provided.

## Interpretation Guidance

- Check filter selections before interpreting charts.
- Distinguish sales, cost and gross profit.
- Lead time is derived from order and ship dates.
- Factory-specific savings are not established.
- Model metrics have an unresolved discrepancy.

## Troubleshooting

1. Confirm that the virtual environment is activated.
2. Install dependencies from requirements.txt.
3. Confirm that app.py exists.
4. Confirm that required data and model files are present.
5. Review the terminal error message.

Do not delete data or model files to resolve an error
without first creating a backup.