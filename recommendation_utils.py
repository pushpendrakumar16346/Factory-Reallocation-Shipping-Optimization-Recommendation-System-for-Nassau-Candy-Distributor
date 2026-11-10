
import pandas as pd


def rank_existing_priorities(
    data,
    score_column="Balanced_Score",
    top_n=5
):
    """
    Rank existing product review scores.
    This is not a factory-feasibility or factory-benefit ranking.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if score_column not in data.columns:
        raise ValueError(f"Score column not found: {score_column}")

    if top_n < 1:
        raise ValueError("top_n must be at least 1.")

    result = data.copy()
    result[score_column] = pd.to_numeric(
        result[score_column], errors="coerce"
    )

    result = result.dropna(subset=[score_column])

    result = result.sort_values(
        by=score_column,
        ascending=False,
        kind="mergesort"
    )

    result = result.head(top_n).reset_index(drop=True)
    result.insert(0, "App_Review_Priority_Rank", range(1, len(result) + 1))

    result["App_Ranking_Interpretation"] = (
        "Existing product review priority; not factory benefit or feasibility"
    )

    return result


def get_factory_option_warnings(option_data):
    """Return factory options that must remain flagged as unverified."""
    required = [
        "Product Name",
        "Reference Factory",
        "Factory Option",
        "Compatibility_Status",
        "Recommendation_Status"
    ]

    missing = [col for col in required if col not in option_data.columns]

    if missing:
        raise ValueError(f"Missing factory option columns: {missing}")

    result = option_data.copy()

    if "Is_Reference_Mapping" in result.columns:
        result["App_Option_Interpretation"] = result[
            "Is_Reference_Mapping"
        ].map({
            True: "Reference mapping only; actual dispatch not verified",
            False: "Unverified alternative; do not treat as approved"
        })

    return result
