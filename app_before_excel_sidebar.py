
import json
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Nassau Candy Analytics",
    page_icon="🍬",
    layout="wide"
)

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / "data"
REPORT_DIR = BASE / "reports"

st.markdown("""
<style>
.main {background-color: #f7f8fc;}
.block-container {padding-top: 1.5rem;}
[data-testid="stMetric"] {
    background: white;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #e7eaf0;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_transactions():
    config_path = BASE / "app_config.json"

    with open(config_path, encoding="utf-8") as f:
        config = json.load(f)

    path = Path(config["data_path"])

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    df["_Order_Date"] = pd.to_datetime(
        df["Order Date"], dayfirst=True, errors="coerce"
    )
    df["_Ship_Date"] = pd.to_datetime(
        df["Ship Date"], dayfirst=True, errors="coerce"
    )
    df["_Lead_Time_Days"] = (
        df["_Ship_Date"] - df["_Order_Date"]
    ).dt.days

    for col in ["Sales", "Units", "Gross Profit", "Cost"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


@st.cache_data
def load_supporting_files():
    result = {}

    for path in DATA_DIR.rglob("*.csv"):
        try:
            result[path.stem] = pd.read_csv(path)
        except Exception:
            continue

    return result


def money(value):
    return f"${value:,.2f}"


def safe_mean(series):
    return series.mean() if series.notna().any() else np.nan


def show_downloads(data):
    st.subheader("Download analysis")

    st.download_button(
        "Download filtered data (CSV)",
        data.to_csv(index=False).encode("utf-8"),
        "nassau_filtered_analysis.csv",
        "text/csv"
    )

    output = data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download analysis report (CSV)",
        output,
        "nassau_analysis_report.csv",
        "text/csv"
    )


try:
    df = load_transactions()
except Exception as error:
    st.error(f"Unable to load application data: {error}")
    st.stop()


required = [
    "Order ID", "Product Name", "Region", "Ship Mode",
    "Sales", "Units", "Gross Profit", "Cost"
]

missing = [c for c in required if c not in df.columns]

if missing:
    st.error(f"Required dataset columns are missing: {missing}")
    st.stop()


supporting = load_supporting_files()

st.title("🍬 Nassau Candy Analytics")
st.caption("Sales, profitability, shipping and operational analysis")

pages = [
    "Home",
    "Product Performance",
    "Region Analysis",
    "Ship Mode Analysis",
    "Factory Explorer",
    "Scenario Simulator",
    "Recommendations",
    "Risk and Impact"
]

page = st.sidebar.radio("Navigation", pages)

st.sidebar.header("Dashboard Filters")

products = sorted(df["Product Name"].dropna().unique())
regions = sorted(df["Region"].dropna().unique())
ship_modes = sorted(df["Ship Mode"].dropna().unique())

selected_products = st.sidebar.multiselect(
    "Products", products, default=products
)
selected_regions = st.sidebar.multiselect(
    "Regions", regions, default=regions
)
selected_modes = st.sidebar.multiselect(
    "Ship modes", ship_modes, default=ship_modes
)

if not selected_products or not selected_regions or not selected_modes:
    st.warning("Your filters returned no selections. Select at least one value in each filter.")
    st.stop()

filtered = df[
    df["Product Name"].isin(selected_products)
    & df["Region"].isin(selected_regions)
    & df["Ship Mode"].isin(selected_modes)
].copy()

if filtered.empty:
    st.warning("No records match the selected filters. Adjust your filters.")
    st.stop()

sales = filtered["Sales"].sum()
profit = filtered["Gross Profit"].sum()
units = filtered["Units"].sum()
orders = filtered["Order ID"].nunique()
lead_time = safe_mean(filtered["_Lead_Time_Days"])
margin = profit / sales * 100 if sales else np.nan


if page == "Home":
    st.header("Business Performance Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Sales", money(sales))
    c2.metric("Gross Profit", money(profit))
    c3.metric("Units Sold", f"{units:,.0f}")
    c4.metric("Orders", f"{orders:,}")

    c5, c6 = st.columns(2)
    c5.metric(
        "Profit Margin",
        f"{margin:.2f}%" if np.isfinite(margin) else "Not available"
    )
    c6.metric(
        "Average Derived Lead Time",
        f"{lead_time:.2f} days" if np.isfinite(lead_time) else "Not available"
    )

    left, right = st.columns(2)

    with left:
        product_sales = (
            filtered.groupby("Product Name", as_index=False)["Sales"]
            .sum().sort_values("Sales", ascending=False)
        )
        st.plotly_chart(
            px.bar(product_sales, x="Product Name", y="Sales",
                   title="Sales by Product"),
            use_container_width=True
        )

    with right:
        region_sales = (
            filtered.groupby("Region", as_index=False)["Sales"]
            .sum().sort_values("Sales", ascending=False)
        )
        st.plotly_chart(
            px.bar(region_sales, x="Region", y="Sales",
                   title="Sales by Region"),
            use_container_width=True
        )


elif page == "Product Performance":
    st.header("Product Performance")

    product_summary = (
        filtered.groupby("Product Name", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Gross_Profit=("Gross Profit", "sum"),
            Units=("Units", "sum"),
            Orders=("Order ID", "nunique")
        )
    )

    product_summary["Profit Margin (%)"] = np.where(
        product_summary["Sales"] != 0,
        product_summary["Gross_Profit"] /
        product_summary["Sales"] * 100,
        np.nan
    )

    st.dataframe(
        product_summary.sort_values("Sales", ascending=False),
        use_container_width=True
    )

    st.plotly_chart(
        px.bar(
            product_summary.sort_values("Sales", ascending=False),
            x="Product Name", y="Sales",
            title="Product Sales Comparison"
        ),
        use_container_width=True
    )

    st.plotly_chart(
        px.scatter(
            product_summary,
            x="Sales",
            y="Gross_Profit",
            size="Units",
            hover_name="Product Name",
            title="Product Sales and Profit Relationship"
        ),
        use_container_width=True
    )


elif page == "Region Analysis":
    st.header("Regional Analysis")

    region_summary = (
        filtered.groupby("Region", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Gross_Profit=("Gross Profit", "sum"),
            Units=("Units", "sum"),
            Orders=("Order ID", "nunique")
        )
    )

    region_summary["Profit Margin (%)"] = np.where(
        region_summary["Sales"] != 0,
        region_summary["Gross_Profit"] /
        region_summary["Sales"] * 100,
        np.nan
    )

    st.dataframe(region_summary, use_container_width=True)

    st.plotly_chart(
        px.bar(region_summary, x="Region", y="Sales",
               title="Sales by Region"),
        use_container_width=True
    )


elif page == "Ship Mode Analysis":
    st.header("Shipping Analysis")

    ship_summary = (
        filtered.groupby("Ship Mode", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Gross_Profit=("Gross Profit", "sum"),
            Orders=("Order ID", "nunique"),
            Average_Lead_Time=("_Lead_Time_Days", "mean")
        )
    )

    st.dataframe(ship_summary, use_container_width=True)

    st.plotly_chart(
        px.bar(ship_summary, x="Ship Mode", y="Orders",
               title="Orders by Shipping Mode"),
        use_container_width=True
    )

    st.plotly_chart(
        px.bar(ship_summary, x="Ship Mode",
               y="Average_Lead_Time",
               title="Average Derived Lead Time by Ship Mode"),
        use_container_width=True
    )

    st.caption(
        "Lead time is calculated from Ship Date minus Order Date. "
        "It is not independently verified carrier transit time."
    )


elif page == "Factory Explorer":
    st.header("Factory Reference Explorer")

    factory_files = {
        name: data for name, data in supporting.items()
        if "factory" in name.lower()
    }

    if not factory_files:
        st.info("No factory reference CSV was found in the application data folder.")
    else:
        for name, data in factory_files.items():
            st.subheader(name.replace("_", " ").title())
            st.dataframe(data, use_container_width=True)

    st.info(
        "Factory selection is for exploring reference information. "
        "The prediction model does not use factory as an input feature. "
        "Alternative factory savings are not established by this dashboard."
    )


elif page == "Scenario Simulator":
    st.header("Scenario Simulator")

    st.write(
        "Explore illustrative changes to sales, cost and profit. "
        "These controls do not represent a probability of success."
    )

    sales_change = st.slider(
        "Illustrative sales change (%)", -30, 50, 0
    )
    cost_change = st.slider(
        "Illustrative cost change (%)", -30, 50, 0
    )
    speed_profit_priority = st.slider(
        "Speed versus profit priority",
        0, 100, 50
    )

    scenario_sales = sales * (1 + sales_change / 100)
    scenario_cost = filtered["Cost"].sum() * (
        1 + cost_change / 100
    )
    scenario_profit = scenario_sales - scenario_cost

    a, b, c = st.columns(3)
    a.metric("Scenario Sales", money(scenario_sales))
    b.metric("Scenario Cost", money(scenario_cost))
    c.metric("Scenario Profit", money(scenario_profit))

    comparison = pd.DataFrame({
        "Metric": ["Sales", "Cost", "Profit"],
        "Baseline": [
            sales,
            filtered["Cost"].sum(),
            profit
        ],
        "Scenario": [
            scenario_sales,
            scenario_cost,
            scenario_profit
        ]
    })

    st.plotly_chart(
        px.bar(
            comparison.melt(
                id_vars="Metric",
                var_name="Case",
                value_name="Amount"
            ),
            x="Metric",
            y="Amount",
            color="Case",
            barmode="group",
            title="Baseline versus Scenario"
        ),
        use_container_width=True
    )

    st.write(
        f"Selected speed-profit priority: {speed_profit_priority}/100"
    )
    st.caption(
        "The priority slider records a preference setting; it does not "
        "calculate an optimized or validated recommendation."
    )


elif page == "Recommendations":
    st.header("Recommendation Dashboard")

    recommendation_files = {
        name: data for name, data in supporting.items()
        if any(term in name.lower() for term in [
            "recommend", "priority", "opportunity"
        ])
    }

    if recommendation_files:
        for name, data in recommendation_files.items():
            st.subheader(name.replace("_", " ").title())
            st.dataframe(data, use_container_width=True)

            st.download_button(
                f"Download {name}",
                data.to_csv(index=False).encode("utf-8"),
                f"{name}.csv",
                "text/csv",
                key=f"download_{name}"
            )
    else:
        st.info(
            "No recommendation export was detected. "
            "The dashboard will show descriptive product and region rankings."
        )

        product_ranking = (
            filtered.groupby("Product Name", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum")
            )
            .sort_values("Gross_Profit", ascending=False)
        )

        st.subheader("Products ranked by observed gross profit")
        st.dataframe(product_ranking, use_container_width=True)

        st.caption(
            "Rankings are descriptive, not proof of optimal decisions."
        )

    recommendation_download = (
        product_ranking.to_csv(index=False).encode("utf-8")
        if "product_ranking" in locals()
        else filtered.to_csv(index=False).encode("utf-8")
    )

    st.download_button(
        "Download current product ranking",
        data=recommendation_download,
        file_name="nassau_recommendations.csv",
        mime="text/csv"
    )


elif page == "Risk and Impact":
    st.header("Risk and Impact Analysis")

    risk_files = {
        name: data for name, data in supporting.items()
        if any(term in name.lower() for term in [
            "risk", "sensitivity", "impact"
        ])
    }

    if risk_files:
        for name, data in risk_files.items():
            st.subheader(name.replace("_", " ").title())
            st.dataframe(data, use_container_width=True)
    else:
        st.info("No exported risk analysis file was detected.")

    st.subheader("Observed business exposure")

    region_exposure = (
        filtered.groupby("Region", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Gross_Profit=("Gross Profit", "sum"),
            Orders=("Order ID", "nunique")
        )
    )

    st.dataframe(region_exposure, use_container_width=True)

    st.caption(
        "This panel presents observed sales and profit exposure. "
        "It does not claim a quantified probability of operational failure."
    )


st.divider()

st.subheader("Export filtered analysis")

st.download_button(
    "Download filtered analysis CSV",
    filtered.to_csv(index=False).encode("utf-8"),
    "nassau_filtered_analysis.csv",
    "text/csv"
)

from io import BytesIO

excel_buffer = BytesIO()

with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
    filtered.to_excel(
        writer,
        sheet_name="Filtered Transactions",
        index=False
    )

    filtered.groupby("Product Name", as_index=False).agg(
        Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Units=("Units", "sum")
    ).to_excel(
        writer,
        sheet_name="Product Analysis",
        index=False
    )

    filtered.groupby("Region", as_index=False).agg(
        Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    ).to_excel(
        writer,
        sheet_name="Region Analysis",
        index=False
    )

st.download_button(
    "Download analysis Excel",
    data=excel_buffer.getvalue(),
    file_name="nassau_dashboard_analysis.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.caption(
    "Analysis is based on the selected records. "
    "Recommendations are indicative and not proven optimal."
)
