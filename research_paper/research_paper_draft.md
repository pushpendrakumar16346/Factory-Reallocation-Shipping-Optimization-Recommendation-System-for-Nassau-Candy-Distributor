Data-Driven Analysis of Product, Regional, Shipping, and Factory-Reference Performance at Nassau Candy Distributor

A Data Analytics, Predictive Modelling, Clustering, and Decision-Support Study

---

# Abstract

This research presents a data-driven analysis of product, regional, shipping,
and factory-reference performance at Nassau Candy Distributor. The study uses
a dataset containing 10,194 records and 18 original variables to examine
business patterns, assess data quality, engineer analytical features, and
develop decision-support insights.

The analytical methodology includes exploratory data analysis, lead-time
predictive modelling, clustering, factory-reference analysis, scenario
simulation, profitability sensitivity analysis, optimization recommendations,
and KPI and risk assessment. A Streamlit dashboard was also developed to
present key findings, interactive analyses, and decision-support information.

The study aims to support a better understanding of product performance,
regional patterns, shipping characteristics, and factory-reference options.
It also demonstrates how predictive analytics and analytical tools can support
business review and planning. However, factory-reference mappings are treated
as reference information rather than verified historical dispatch records,
and scenario outputs are interpreted within the limits of available evidence.

The findings provide an analytical foundation for business review and future
investigation. The study also identifies data and methodological limitations
that should be considered before operational decisions are made.

---

# Introduction

The distribution industry involves several interconnected business activities,
including product management, order processing, shipping, regional distribution,
and supply chain coordination. Analysing these activities is important for
understanding business performance and identifying opportunities for improvement.

Nassau Candy Distributor provides the business context for this research. The
project uses historical business data to examine product performance, regional
patterns, shipping characteristics, and factory-reference information.

Traditional reporting methods can describe past business performance, but
analytical techniques can provide additional insights. Exploratory data analysis
helps identify patterns and relationships, predictive modelling supports the
examination of lead-time behaviour, and clustering helps identify groups of
similar business records. Scenario simulation and optimization methods can
further support structured business evaluation.

This research applies a combination of data analytics, machine learning,
statistical analysis, and decision-support techniques to the available Nassau
Candy Distributor dataset. It also presents the results through an interactive
Streamlit dashboard.

The overall purpose is to develop a structured analytical framework that helps
interpret business data, evaluate operational patterns, and support informed
management review. The research also considers the limitations of the available
data to ensure that analytical findings are not interpreted as unsupported
operational guarantees.

---

# Business Background

Nassau Candy Distributor is the business context for this research project.
The distribution business involves managing products, customer orders,
shipment activities, and the movement of goods across different regions.

Effective distribution management requires an understanding of product demand,
sales performance, order characteristics, shipping methods, and delivery-related
patterns. Analysing these areas can help identify differences in business
performance and provide useful information for management review.

This project examines historical transaction-level data associated with
Nassau Candy Distributor. The analysis focuses on product performance,
regional performance, shipping performance, factory-reference analysis,
and business decision support.

The project combines descriptive analytics, predictive modelling, clustering,
scenario simulation, profitability sensitivity analysis, and optimization-
oriented methods. These techniques are presented through an interactive
Streamlit dashboard to make the analytical results easier to explore.

An important consideration is that the available dataset does not establish
every operational detail. Factory-reference mappings should not be interpreted
as verified historical dispatch records, and alternative factory scenarios
should not be treated as confirmed cost savings or operational improvements.
The analysis therefore distinguishes observed data from assumptions and areas
requiring further validation.

---

# Problem Statement

The availability of historical business data creates opportunities to
understand product performance, regional differences, shipping characteristics,
and operational patterns. However, raw transaction data alone does not
automatically provide clear and actionable business insights.

The main problem addressed by this research is the need to transform the
available Nassau Candy Distributor dataset into a structured analytical
framework that can support business performance evaluation and informed
decision-making.

The research examines product-level sales and profitability, regional
performance, shipping methods, order lead-time behaviour, predictive modelling,
clustering, factory-reference mappings, scenario simulation, profitability
sensitivity, optimization recommendations, and business risks.

A further challenge is ensuring that analytical conclusions remain consistent
with the available evidence. Reference factory mappings do not establish actual
historical dispatch decisions, and scenario simulations cannot independently
confirm factory-specific cost savings or operational improvements.

Therefore, the research focuses on developing reliable analytical insights
while clearly distinguishing measured results, model-based estimates,
reference information, and assumptions requiring additional validation.

---

# Research Objectives

The primary objective of this research is to develop a data-driven analytical
framework for examining product, regional, shipping, and factory-reference
performance at Nassau Candy Distributor.

The specific objectives are:

1. To understand the structure, characteristics, and quality of the available
   business dataset.
2. To perform exploratory data analysis to examine product, regional, shipping,
   sales, and profitability patterns.
3. To engineer relevant analytical features from the original business data.
4. To develop and evaluate a predictive model for analysing order lead-time
   behaviour.
5. To apply clustering techniques to identify groups of similar business
   observations.
6. To examine product-to-factory reference mappings and evaluate alternative
   factory options using the available evidence.
7. To conduct scenario simulation and profitability sensitivity analysis.
8. To develop optimization-oriented recommendations and assess relevant
   business KPIs and risks.
9. To create an interactive Streamlit dashboard for communicating analytical
   results and supporting business review.
10. To identify limitations and opportunities for future research.

---

# Research Questions

This research is guided by the following questions:

1. What patterns can be identified in product-level sales and profitability?
2. How does business performance vary across geographical regions?
3. What patterns are visible across shipping methods and order lead times?
4. Can historical business features support predictive modelling of order
   lead-time behaviour?
5. Can clustering identify meaningful groups within the available business
   observations?
6. What insights can be obtained from product-to-factory reference mappings?
7. How can alternative factory scenarios be assessed when factory-specific
   evidence is incomplete?
8. How can profitability sensitivity and optimization-oriented analysis
   support business review?
9. How can an interactive dashboard improve access to analytical findings?
10. What data limitations should be considered before operational decisions
    are made?

---

# Dataset Description

The research uses the Nassau Candy Distributor dataset supplied for this
project.

The original dataset contains 10,194 records and 18 columns. The processed
analytical dataset contains 10,194 records and 34 columns after the project's
data preparation and feature engineering activities.

The data includes business information used to examine products, orders,
sales, profitability, geographical regions, shipping characteristics, and
related analytical variables.

The original dataset is retained separately from the processed dataset to
preserve data traceability. Date fields are interpreted using day-first
parsing where required, without unnecessarily overwriting the original date
strings.

The processed dataset supports exploratory analysis, predictive modelling,
clustering, scenario evaluation, and dashboard reporting.

The predictive model uses 20 predictor features. Factory information is not
included as a predictor in that model.

The dataset represents the records available for this study. It should not
automatically be interpreted as a complete representation of every
operational event or supply-chain decision made by the business.

---

# Data Quality Methodology

Data quality assessment was conducted before the main analytical activities.
The purpose was to identify issues that could affect the reliability and
interpretation of the results.

The assessment included:

- Inspection of dataset dimensions and column names.
- Review of data types and expected variable formats.
- Identification of missing values.
- Examination of duplicate records.
- Validation of date fields and date parsing.
- Review of numeric variables and unusual values.
- Examination of categorical values and inconsistent labels.
- Validation of important derived variables.

Original data was preserved to support traceability. Transformations were
performed in the processed dataset rather than silently changing the raw
source.

Date parsing followed the day-first format where appropriate. Lead time was
calculated as the difference between Ship Date and Order Date. Negative or
otherwise invalid calculated values were considered during validation.

Lead time in this research represents the interval between the recorded
order date and ship date. It is not an independently verified measure of
carrier transit time.

Data quality checks were used to improve consistency and reduce the risk of
misleading analytical conclusions. Remaining limitations were documented
rather than hidden.

---

# Feature Engineering Methodology

Feature engineering was used to transform the original business variables
into features suitable for descriptive and predictive analysis.

The process included date-related feature preparation, financial feature
calculations, safe numerical operations, and model feature preparation.

Order-date features were derived to support the examination of temporal
patterns. Financial features were prepared to support revenue and
profitability analysis. Safe division methods were used where ratios or
other division-based measures were required, helping avoid invalid
calculations caused by zero denominators.

Lead time was calculated using the recorded Ship Date and Order Date.
Additional lead-time categories were used for grouped analysis.

The model preparation process selected 20 predictor features for the
lead-time prediction pipeline. Factory was not included as a model
predictor.

Feature engineering was performed with attention to data types, missing
values, and consistency between training and prediction workflows.

Derived features are analytical representations of the available source
data. They should not be interpreted as independently verified operational
measurements.

---

# Exploratory Data Analysis Results

Exploratory data analysis was conducted to understand the characteristics
and patterns of the available business data.

The analysis examined product performance, regional performance, shipping
methods, sales, profitability, and lead-time behaviour.

Product-level analysis was used to compare business performance across
products. Regional analysis examined geographical differences in the
available records. Shipping analysis compared order characteristics and
lead-time patterns across shipping methods.

Financial analysis provided a basis for reviewing sales and profitability
indicators. Visualizations and summary statistics were used to make
patterns easier to interpret.

The exploratory analysis provides the descriptive foundation for the
subsequent predictive, clustering, scenario, and decision-support
activities.

The final submitted paper should include the verified numerical findings
and relevant charts from the exploratory analysis notebook. In particular,
the following values should be inserted from the actual outputs:

- Leading products by the selected sales or profitability measure:
  Product-level analysis identified Wonka Bar - Triple Dazzle Caramel as the highest-sales product, with total sales of $28,485.00. Wonka Bar -Scrumdiddlyumptious followed with $27,874.80, and Wonka Bar - Milk Chocolate recorded $26,867.75. Product-level results also showed substantial variation in sales volume and gross-profit contribution.
- Regional performance observations:
  The Pacific region recorded the highest sales at $46,301.53 and gross profit of $30,485.94 across 3,253 records. Atlantic followed with sales of $41,197.24 and gross profit of $26,973.70. Gulf recorded the lowest regional sales at $22,247.26. Regional gross-profit margins were relatively similar, ranging from approximately 65.47% to 66.43%.
- Shipping method comparisons:
  Standard Class represented the largest shipping category, with 6,120 records, 5,142 unique orders, sales of $85,490.35, and gross profit of $56,424.46. Second Class recorded sales of $27,860.22, First Class $21,319.39, and Same Day $7,113.67. The mean date-derived lead-time values varied across shipping categories, but these differences should not be interpreted as verified carrier transit performance.
- Overall sales and profitability observations:
  The dataset contained total sales of $141,783.63, total cost of $48,340.83, and supplied gross profit of $93,442.80. The weighted gross-profit margin was 65.9052%. Gross profit was retained as supplied in the original dataset, and the financial analysis treated historical results separately from hypothetical cost-sensitivity scenarios.
- Lead-time distribution and notable patterns:
  The derived Lead_Time_Days variable had a mean of 1,320.84 days, a median of 1,274 days, a standard deviation of 262.44 days, and a range from 904 to 1,642 days. It was calculated as Ship Date minus Order Date. These unusually long values have not been verified as actual carrier transit durations and must be interpreted as date-derived measures.

No numerical ranking or business conclusion should be added unless it is
supported by the completed analysis.

---

# Predictive Modelling Methodology

Predictive modelling was used to examine lead-time behaviour using the
available historical business features.

The modelling workflow included preparing the target variable, selecting
predictor features, preparing the input data, defining a machine learning
pipeline, training the model, and saving the resulting model artifact.

The model uses 20 predictor features. Factory information is not included
as a predictor.

A pipeline-based approach was used to maintain consistency between model
preparation and prediction. The saved model artifact was subsequently
reloaded to verify that it could be used outside the original training
session.

The modelling process was designed to support reproducibility and
consistent prediction behaviour. Repeated predictions and predictions
after reloading the saved pipeline were compared during validation.

The model estimates lead-time behaviour based on the features and
relationships represented in the available dataset. Its predictions
should be interpreted as model estimates rather than guaranteed future
delivery outcomes.

---

# Model Evaluation

Model evaluation was performed to assess the predictive performance and
reliability of the lead-time modelling workflow.

Evaluation should be based on the actual metrics generated by the
completed modelling notebook. Relevant regression measures may include
Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared
Error (RMSE), and the coefficient of determination (R-squared), where
these were calculated in the project.

The model artifact was reloaded successfully as a machine learning
Pipeline. Prediction reproducibility was also checked by comparing
repeated predictions and predictions made after reloading the saved
artifact.

The following verified results must be inserted before final submission:

- Model algorithm: Tuned Random Forest Regressor
- MAE: 95.9795 (saved model metadata; see discrepancy note)
- MSE: Not separately reported in the saved model evaluation outputs
- RMSE: 120.7382 (saved model metadata; see discrepancy note)
- R-squared: 0.7929 (saved model metadata; see discrepancy note)
- Test dataset size: 2,062 records (saved model metadata)

If multiple model evaluation outputs differ, the discrepancy should be
documented and investigated. Values must not be silently reconciled or
replaced with estimates.

Evaluation metrics describe performance under the project's evaluation
conditions. They do not guarantee the same accuracy on future or
substantially different business data.

---

# Clustering Methodology

Clustering analysis was performed to identify groups of similar business
observations based on selected analytical features.

The purpose of clustering was to explore patterns that may not be
immediately visible through individual variables or conventional summary
statistics.

The workflow involved selecting relevant variables, preparing the data,
applying the clustering approach used in the project, and examining the
resulting group characteristics.

Cluster profiles were reviewed to understand how groups differed across
the selected business dimensions. Appropriate visualizations and summary
statistics were used to support interpretation.

The resulting clusters represent similarities within the selected data
and features. They should not automatically be interpreted as official
business segments, customer types, or operational categories without
additional business validation.

The final paper should report the actual clustering algorithm, selected
features, number of clusters, and verified cluster characteristics from
the completed clustering notebook.

---

# Factory Reference Analysis

Factory-reference analysis examined the relationship between products
and their associated factory reference information.

The purpose was to understand the available product-to-factory mapping
and review alternative factory options within the limits of the data.

The analysis distinguishes the reference factory mapping from verified
historical dispatch information. A product-to-factory mapping indicates
a reference relationship in the available data; it does not independently
prove that a particular factory fulfilled a specific historical order.

Alternative factory options were reviewed using available compatibility
and recommendation information. These options require additional
operational validation before they can be treated as feasible production
or distribution alternatives.

The analysis therefore focuses on organizing available reference
information and identifying options that may warrant further
investigation. It does not establish actual factory capacity, confirmed
dispatch history, or guaranteed operational improvements.

---

# Scenario Simulation

Scenario simulation was used to examine alternative analytical
conditions and support structured business review.

The simulation process considered available factory-option information
and relevant supporting evidence. The project included checks for
factory-specific lead-time estimability, factory-specific cost
availability, and capacity data availability.

A scenario was treated as requiring further validation when the necessary
factory-specific evidence was available. Where the evidence was
incomplete, the scenario was classified as having insufficient
factory-specific support.

The scenario assessment deliberately avoids inventing factory-specific
lead-time changes, cost savings, or probabilities of success when these
cannot be supported by the available information.

Scenario outputs should therefore be interpreted as structured
assessments of available evidence, not as confirmed forecasts or
operational guarantees.

---

# Optimization Methodology

Optimization-oriented analysis was conducted to organize business
priorities and support evidence-based review.

The methodology used available performance indicators and recommendation
scores to rank or prioritize existing business observations for further
investigation.

Existing product review priorities were interpreted as analytical
priorities rather than proof of factory benefit, operational feasibility,
or guaranteed financial improvement.

The project also examined factory-option information and supporting
evidence to distinguish options that may require additional validation
from options for which the available evidence is insufficient.

The recommendations are indicative and depend on the quality and
completeness of the available dataset. They should be reviewed alongside
business constraints, operational knowledge, capacity information, and
verified cost data before implementation.

The analysis does not claim to identify a mathematically proven global
optimum or a guaranteed best factory allocation.

---

# KPI and Risk Analysis

KPI and risk analysis was conducted to organize important business
indicators and highlight areas requiring management attention.

The analysis considered available indicators associated with product
performance, regional performance, shipping, lead time, profitability,
and factory-reference evaluation.

Risk assessment focused on interpreting analytical findings within
the limits of the available evidence. Particular attention was given
to data quality, model uncertainty, factory-specific evidence gaps,
and the distinction between reference mappings and actual operational
records.

The project recognizes that a predictive estimate is not a guaranteed
business outcome. Similarly, scenario support does not establish a
probability of success, and an indicative recommendation does not
prove operational feasibility.

The KPI and risk analysis is intended to support monitoring and
structured review. Final KPI definitions, thresholds, and management
actions should be aligned with verified business requirements.

---

# Dashboard Description

An interactive Streamlit dashboard was developed to communicate the
project's analytical findings and provide a practical interface for
exploring the available data.

The dashboard contains eight main pages:

1. Home
2. Product Performance
3. Region Analysis
4. Ship Mode Analysis
5. Factory Explorer
6. Scenario Simulator
7. Recommendations
8. Risk and Impact

The application includes relevant filters for product, region, and
shipping method. It also presents KPI cards, charts, scenario controls,
recommendation panels, and risk information.

CSV and Excel export functionality is provided to support further
review of the analytical data.

The application uses reusable utility modules for prediction,
feature preparation, scenario assessment, and recommendation logic.
Validation checks were performed on the application source, model
loading, filters, scenario logic, and data export functionality.

The dashboard is a decision-support interface. It does not replace
business validation, operational planning, or management approval.

---

# Results and Discussion

The project combines descriptive analytics, predictive modelling,
clustering, factory-reference analysis, scenario simulation,
profitability sensitivity analysis, optimization-oriented
recommendations, and KPI and risk assessment.

The exploratory analysis provides an overview of product, regional,
financial, and shipping patterns in the available records. Feature
engineering prepares the dataset for further analytical activities.

The lead-time modelling workflow demonstrates how historical business
features can be used to estimate lead-time behaviour. Model
reproducibility and artifact reload checks provide additional evidence
that the modelling workflow can be reused consistently.

Clustering provides a way to examine similarities between business
observations. Factory-reference analysis organizes available mapping
information, while scenario simulation distinguishes supported
assessments from options that require additional evidence.

The recommendation and risk analysis translates analytical outputs
into structured areas for business review. The Streamlit dashboard
makes these outputs accessible through interactive pages and
downloadable reports.

The overall contribution is an integrated analytical workflow that
connects data preparation, analysis, modelling, and decision support.

The final discussion should incorporate the verified numerical
results, model evaluation metrics, cluster profiles, and most
important findings from the completed project notebooks. Any
differences between evaluation outputs should be disclosed rather
than concealed.

---

# Research Limitations

This research has several limitations that should be considered when
interpreting its findings.

First, the analysis is limited to the information contained in the
available dataset. Missing, incomplete, or unrecorded business
information may affect the interpretation of results.

Second, calculated lead time is based on the difference between the
recorded Ship Date and Order Date. It is not an independently verified
measure of carrier transit time.

Third, the product-to-factory relationship is treated as reference
mapping information. It does not establish verified historical
dispatch or fulfilment decisions.

Fourth, factory-specific capacity, cost, and lead-time evidence may
not be available for every alternative factory option. Consequently,
scenario assessments cannot establish confirmed factory-specific
savings or operational improvements.

Fifth, Haversine distances represent straight-line geographical
distances. They do not represent actual road distances, freight routes,
or transportation costs.

Sixth, model performance depends on the available data, selected
features, and evaluation methodology. Predictive results should not
be treated as guaranteed future outcomes.

Seventh, clustering results depend on the selected features and
clustering methodology. Identified groups require business
interpretation and validation.

Finally, optimization-oriented recommendations are indicative
priorities rather than proven globally optimal decisions. Additional
operational and financial information is needed before implementation.

---

# Future Scope

Future research can extend this project by incorporating additional
operational and business information.

Potential improvements include:

- Integrating verified historical factory dispatch and fulfilment
  records.
- Incorporating factory-specific production capacity and availability.
- Collecting verified manufacturing and transportation cost data.
- Including actual road and freight-route distances instead of relying
  only on straight-line geographical distances.
- Incorporating carrier transit events and delivery confirmation dates.
- Testing additional predictive models and evaluating them using
  consistent validation procedures.
- Monitoring model performance as new business data becomes available.
- Investigating additional clustering methods and validating cluster
  interpretations with business stakeholders.
- Developing more comprehensive scenario simulations using verified
  operational constraints.
- Extending optimization analysis with validated cost, capacity,
  compatibility, and service-level constraints.
- Establishing formal KPI definitions and monitoring thresholds.
- Improving dashboard deployment, access control, and automated data
  refresh processes.

These improvements could increase the practical value of the analytical
framework and support more detailed operational decision-making.

---

# Conclusion

This research developed a data-driven analytical framework for
examining product, regional, shipping, and factory-reference
performance at Nassau Candy Distributor.

Using a dataset containing 10,194 records and 18 original columns,
the project carried out data quality assessment, feature engineering,
exploratory data analysis, lead-time predictive modelling, clustering,
factory-reference analysis, scenario simulation, profitability
sensitivity analysis, optimization-oriented recommendations, and
KPI and risk assessment.

An interactive Streamlit dashboard was also developed to present
analytical findings through eight main pages, filters, visualizations,
scenario controls, and downloadable reports.

The project demonstrates how different analytical techniques can
be combined into a structured decision-support workflow. It also
emphasizes the importance of interpreting results according to the
evidence available.

In particular, reference factory mappings should not be treated
as verified dispatch records, scenario assessments should not be
interpreted as guaranteed cost savings, and predictive estimates
should not be considered certain future outcomes.

Overall, the research provides an analytical foundation for business
review and identifies areas where additional operational data and
validation could strengthen future decision-making.

---

# References

The following references provide methodological background for
the analytical techniques and software used in this project.
The exact software versions and project-specific sources should
be verified before final submission.

1. James, G., Witten, D., Hastie, T., and Tibshirani, R. (2021).
   An Introduction to Statistical Learning: With Applications in R.
   Second Edition. Springer.

2. Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011).
   Scikit-learn: Machine Learning in Python.
   Journal of Machine Learning Research, 12, 2825–2830.

3. McKinney, W. (2010).
   Data Structures for Statistical Computing in Python.
   Proceedings of the 9th Python in Science Conference.

4. Hunter, J. D. (2007).
   Matplotlib: A 2D Graphics Environment.
   Computing in Science & Engineering, 9(3), 90–95.

5. The pandas development team.
   pandas documentation.
   https://pandas.pydata.org/docs/

6. The scikit-learn developers.
   scikit-learn documentation.
   https://scikit-learn.org/stable/

7. Streamlit, Inc.
   Streamlit documentation.
   https://docs.streamlit.io/

8. Nassau Candy Distributor dataset.
   Original project dataset supplied for this research.
   Add the appropriate source, access details, or institutional
   attribution required by the submission guidelines.

Only include references that were actually consulted and are
relevant to the final submitted research paper.

---

# Final Formatting and Review

Before submitting the research paper, complete the following review:

[ ] Confirm the final title and subtitle.
[ ] Review the abstract for accuracy and completeness.
[ ] Check the introduction and business background.
[ ] Confirm that the problem statement and research questions
    match the completed project.
[ ] Verify dataset dimensions and variable descriptions.
[ ] Add actual data quality findings.
[ ] Verify feature engineering descriptions.
[ ] Insert numerical EDA findings and relevant charts.
[ ] Confirm the actual predictive model algorithm.
[x] Inserted reported model metrics with an explicit reconciliation warning.
[ ] Add actual clustering methodology and cluster findings.
[ ] Verify factory-reference analysis descriptions.
[ ] Confirm scenario simulation evidence limitations.
[ ] Review optimization recommendations.
[ ] Add relevant KPI and risk findings.
[ ] Include dashboard screenshots if required.
[ ] Verify all figures, tables, captions, and numbering.
[ ] Check that every reference was actually consulted.
[ ] Check spelling, grammar, and academic formatting.
[ ] Confirm that no unsupported savings, predictions, or
    operational claims are presented as established facts.
[ ] Save the final paper in the required submission format.

The research paper should follow the formatting and citation
requirements specified by the relevant institution or evaluator.


### Model metric reconciliation note

The saved model metadata reports test MAE of 95.9795, test RMSE
of 120.7382, and R-squared of 0.7929 for 2,062 testing records.
However, the model comparison output reports MAE of 139.6707,
RMSE of 163.6754, and R-squared of 0.6195 for the Tuned Random
Forest. The chronological holdout evaluation reports a further
different result. These values have not been reconciled to a single
evaluation run. They are therefore reported with their respective
source labels and must not be treated as interchangeable or as one
definitive metric set. MSE was not separately reported.

