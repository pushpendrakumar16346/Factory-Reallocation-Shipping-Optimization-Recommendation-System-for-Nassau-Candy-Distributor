# Risk, Limitations and Additional Data Requirements

## Main Limitations

- Lead time is derived from Ship Date minus Order Date.
- Lead time is not independently verified carrier transit time.
- Factory mappings are reference mappings, not verified dispatches.
- Haversine distances are straight-line distances, not freight routes.
- Factory-specific savings have not been established.
- Scenario support is not a probability of success.
- Recommendations are indicative, not proven optimal.
- Model evaluation outputs contain unresolved discrepancies.

## Additional Data Required

| Data | Purpose |
|---|---|
| Carrier pickup timestamps | Establish actual shipping start |
| Actual delivery timestamps | Measure transit performance |
| Factory dispatch records | Verify factory-product assignments |
| Factory capacity | Assess production feasibility |
| Factory utilization | Identify constraints |
| Manufacturing costs | Compare production economics |
| Freight rates | Estimate logistics costs |
| Practical freight routes | Estimate route distances |
| Inventory and stockout data | Understand product availability |
| Customer service data | Evaluate service commitments |
| Model evaluation logs | Reconcile model metrics |

No factory savings, delivery improvements or success probabilities
should be claimed without appropriate operational evidence.