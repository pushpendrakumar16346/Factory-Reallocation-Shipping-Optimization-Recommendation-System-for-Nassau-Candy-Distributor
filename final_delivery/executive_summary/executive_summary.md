# Executive Summary
## Nassau Candy Distributor Analytics Project

### Project Overview

This project analyses historical Nassau Candy Distributor data using
data cleaning, exploratory analysis, feature engineering, predictive
modelling, clustering, factory-reference analysis, scenario simulation
and decision-support methods.

An interactive Streamlit dashboard was developed to make the findings
accessible to business users.

### Business Problem

The project investigates product performance, regional sales,
shipping patterns, profitability and date-derived lead-time patterns.
It also examines whether factory-reference information can support
further operational investigation.

### Dataset

The original dataset contains 10,194 records and 18 columns.
The processed dataset contains 10,194 records and 34 columns.

### Main Findings

- Total sales: $141,783.63.
- Total cost: $48,340.83.
- Gross profit: $93,442.80.
- Weighted gross-profit margin: approximately 65.91%.
- Highest-sales product: Wonka Bar - Triple Dazzle Caramel,
  with sales of $28,485.00.
- Highest-sales region: Pacific, with sales of $46,301.53.
- Lowest-sales region: Gulf, with sales of $22,247.26.
- Largest shipping category: Standard Class, with 6,120 records.

### Predictive Model

The selected algorithm was a Tuned Random Forest Regressor.

Saved model metadata reports:
- MAE: 95.9795
- RMSE: 120.7382
- R-squared: 0.7929
- Test records: 2,062

The model comparison output reports:
- MAE: 139.6707
- RMSE: 163.6754
- R-squared: 0.6195

The chronological holdout output reports:
- MAE: 179.0003
- RMSE: 195.6296
- R-squared: -0.1619

These results come from different saved evaluation outputs and have
not been reconciled. They must not be presented as one consistent
evaluation result. MSE was not separately reported.

### Recommended Actions

1. Review high-sales products and their gross-profit contribution.
2. Investigate regional performance differences.
3. Review shipping performance using verified delivery data.
4. Validate product-to-factory mappings against actual dispatch records.
5. Collect factory capacity, production and cost information.
6. Reconcile model evaluation metrics before operational use.
7. Use the dashboard as a decision-support tool.

### Risks and Limitations

Lead time is calculated as Ship Date minus Order Date and is not
independently verified carrier transit time.

Factory mappings are reference mappings, not confirmed historical
dispatch records. Straight-line distances are not actual freight
routes. Factory-specific savings and scenario success probabilities
have not been established.

Recommendations are indicative, not proven optimal.

### Additional Data Required

- Actual carrier pickup and delivery timestamps.
- Factory production and dispatch records.
- Factory capacity and utilization.
- Factory-specific manufacturing costs.
- Freight rates and practical route distances.
- Inventory and stockout records.
- Customer service-level and delivery performance data.
- Model run logs and evaluation split definitions.

### Conclusion

The project provides an analytical foundation for understanding
product, regional, shipping, financial and factory-reference patterns.

The dashboard makes these findings accessible through an interactive
interface. Further operational data validation is required before
making high-impact factory-allocation, freight-savings or
service-level decisions.