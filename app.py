import duckdb
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Soil Health Analytics", page_icon="🌾", layout="wide"
)

st.title("🌾 Soil Health Analytics Dashboard")
st.markdown("Visualizing agronomic field metrics powered by DuckDB & dbt.")


@st.cache_resource
def load_data():
  conn = duckdb.connect("soil_analytics.duckdb", read_only=True)
  query = """
        SELECT 
            m.*,
            l.region,
            l.latitude,
            l.longitude
        FROM fct_soil_health_metrics m
        LEFT JOIN dim_soil_locations l ON m.location_code = l.location_code
    """
  df = conn.execute(query).df()
  conn.close()
  return df


try:
  df = load_data()

  # Sidebar filters
  st.sidebar.header("Filters")
  selected_region = st.sidebar.selectbox(
      "Select Region", options=["All"] + list(df["region"].dropna().unique())
  )

  filtered_df = df
  if selected_region != "All":
    filtered_df = df[df["region"] == selected_region]

  # Top level metrics
  col1, col2, col3 = st.columns(3)
  col1.metric("Total Samples", len(filtered_df))
  col2.metric("Avg pH Level", round(filtered_df["ph_level"].mean(), 2))
  col3.metric(
      "Avg Organic Matter (%)",
      round(filtered_df["organic_matter_pct"].mean(), 2),
  )

  st.divider()

  # Charts section
  c1, c2 = st.columns(2)

  with c1:
    st.subheader("pH Level Distribution by Region")
    fig_ph = px.box(
        filtered_df, x="region", y="ph_level", color="region", points="all"
    )
    st.plotly_chart(fig_ph, use_container_width=True)

  with c2:
    st.subheader("Organic Matter vs Acidity Class")
    fig_scatter = px.box(
        filtered_df,
        x="acidity_class",
        y="organic_matter_pct",
        color="acidity_class",
        points="all",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

  # Data table view
  st.subheader("📋 Underlying Joined Soil Health Data")
  st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
  st.error(f"Error loading dashboard data: {e}")