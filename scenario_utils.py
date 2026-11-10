
import pandas as pd


def assess_factory_option_support(option_row):
    """
    Assess whether a factory option has evidence for factory-specific
    lead-time and cost estimation.
    """
    lead_time_supported = bool(
        option_row.get("Factory_Specific_Lead_Time_Estimable", False)
    )

    cost_supported = bool(
        option_row.get("Factory_Specific_Cost_Available", False)
    )

    capacity_supported = bool(
        option_row.get("Capacity_Data_Available", False)
    )

    if lead_time_supported and cost_supported and capacity_supported:
        status = "REQUIRES FURTHER VALIDATION"
    else:
        status = "INSUFFICIENT FACTORY-SPECIFIC EVIDENCE"

    return {
        "Lead_Time_Evidence_Available": lead_time_supported,
        "Cost_Evidence_Available": cost_supported,
        "Capacity_Evidence_Available": capacity_supported,
        "Scenario_Support_Status": status,
        "Estimated_Lead_Time_Change_Days": None,
        "Estimated_Cost_Saving": None,
        "Success_Probability": None
    }


def review_factory_options(option_data):
    """Add evidence status without changing source scores or estimates."""
    required = [
        "Factory_Specific_Lead_Time_Estimable",
        "Factory_Specific_Cost_Available",
        "Capacity_Data_Available"
    ]

    missing = [col for col in required if col not in option_data.columns]

    if missing:
        raise ValueError(f"Missing scenario evidence columns: {missing}")

    result = option_data.copy()

    statuses = result.apply(
        lambda row: assess_factory_option_support(row)[
            "Scenario_Support_Status"
        ],
        axis=1
    )

    result["App_Scenario_Support_Status"] = statuses

    return result
