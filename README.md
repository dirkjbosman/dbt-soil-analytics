# 🌾 Soil Health Analytics Engineering Pipeline

I architected an end-to-end modern data stack project designed to transform raw agronomic field measurements into clean, tested data marts and interactive visual soil health monitoring dashboards. Follow, Subscribe & DM me at https://x.com/dirkjbosman or https://www.linkedin.com/in/dirkjbosman/.


## 🌟 Why This Project?
Agricultural data is often trapped in fragmented spreadsheets, making it difficult to assess soil compaction, acidity, and nutrient levels rapidly. This project demonstrates how modern analytics engineering tools can be combined to build a lightweight, high-performance local data warehouse pipeline without the overhead of expensive cloud infrastructure.

* **Business Value:** Empowers agricultural analysts and agronomists to instantly isolate nutrient-deficient regions, track soil acidity trends, and monitor physical compaction risks.
* **Target Audience:** Particularly valuable for agricultural researchers, data engineers and analytics professionals looking for a modular, reproducible local template using **dbt** and **DuckDB**.

---

## 🛠️ Tech Stack
* **Transformation:** [dbt (Data Build Tool)](https://www.getdbt.com/)
* **Database & Compute:** [DuckDB](https://duckdb.org/) (Embedded high-performance OLAP)
* **Package/Env Manager:** [Astral uv](https://github.com/astral-sh/uv)
* **Visualization Layer:** [Streamlit](https://streamlit.io/) & [Plotly](https://plotly.com/)

### dbt Architecture & Modeling Strategy

#### How the dbt Pipeline Was Built
The pipeline follows a strict layered analytics engineering pattern:
- Staging Layer (`stg_soil_samples.sql`): A lightweight view layer that directly references the raw CSV source (`src_soil.yml`). It handles column standardization, type casting, and light data cleaning.
- Dimension Table (`dim_soil_locations.sql`): A table materialization built to isolate static spatial attributes (such as **region**, **latitude**, and **longitude**) mapped to unique location codes.
- Fact Table (`fct_soil_health_metrics.sql`): A table materialization designed to capture transactional agronomic metrics (such as **ph_level**, **organic_matter_pct**, and **nutrient statuses**) tied back to sample IDs and collection dates.

#### Why It Was Modeled This Way (Decision Rationale)
- Star Schema Separation: Separating spatial dimensions (**dim_soil_locations**) from numerical metrics (**fct_soil_health_metrics**) avoids data duplication, ensuring that metadata changes to a region don't require rewriting observation history.
- Declarative Assertions: Built-in dbt tests (`schema.yml`) enforce strict data quality rules (like non-null **sample_id** constraints and accepted values for acidity classes) right inside the build cycle.

#### The Benefits of This Approach
- Modularity & Reusability: Downstream visualization tools (like Streamlit or BI layers) query clean, dependable marts rather than messy raw spreadsheets.
- Performance: Combining dbt with DuckDB pre-calculates transforms locally into columnar storage, rendering dashboard queries instantaneously.
- Maintainability: Clear separation of concerns means business logic changes only need to be updated in a single model file.


---

## 📂 Project Structure

The rough project structure looks as follows:

```text
dbt-soil-analytics/
├── data/
│   └── raw_soil_samples.csv       # Raw field sample inputs (100 records)
├── models/
│   ├── marts/                     # Business-ready analytics tables
│   │   ├── dim_soil_locations.sql
│   │   └── fct_soil_health_metrics.sql
│   ├── staging/                   # Cleaned and standardized views
│   │   ├── src_soil.yml
│   │   └── stg_soil_samples.sql
│   └── schema.yml                 # Data quality test assertions
├── app.py                         # Streamlit interactive dashboard script
├── dbt_project.yml                # dbt configuration
├── profiles.yml                   # DuckDB local adapter settings
└── pyproject.toml                 # Python project dependencies
```

---

## 📊 Dashboard Reporting Explainer

The interactive Streamlit dashboard provides two core analytical views:

1. **pH Level Distribution by Region (Box Plot):** Displays the statistical spread, median, and outlier pH metrics across various agricultural regions (e.g., North Plains, River Valley, Highlands), allowing teams to quickly identify overly acidic or alkaline zones.
2. **Organic Matter vs. Acidity Class (Distribution & Scatter):** Cross-references soil organic matter percentages against classified acidity tiers to evaluate biological fertility alongside chemical composition.

Note: Dashboards are not only just for monitoring, but also to derive insights from. In this particular case, based on your 100-sample dashboard distribution; 
- The River Valley region exhibits a significantly lower average pH level (averaging near 5.2, falling largely into Strongly Acidic territory) compared to the Western Plateau (averaging near 7.5, classifying as Alkaline). 
- Furthermore, neutral soils in this dataset exhibit the highest variance in organic matter content (spanning from 1.5% up to 5.4%), indicating that biological fertility varies widely independent of neutral chemical balances.

### Dashboard Previews

**Full Regional Overview:**
![Full Dashboard View](./dash_1.png)

**Filtered Region View (River Valley):**
![Filtered Dashboard View](./dash_2.png)

---

## 🚀 Quickstart Guide

### 1. Clone and Setup Environment
```bash
git clone [https://github.com/](https://github.com/)<your-username>/dbt-soil-analytics.git
cd dbt-soil-analytics
```

# Install dependencies via uv
```bash
uv init --app --no-readme || true
uv add dbt-duckdb duckdb streamlit plotly
```

### 2. Run dbt Transformations & Data Quality Tests
Execute the pipeline to read raw soil metrics, clean formats, and build analytical marts into DuckDB:
```bash
uv run dbt run --profiles-dir .
uv run dbt test --profiles-dir .
```

### 3. Launch the Interactive Dashboard
Spin up the local Streamlit web application:
```bash
uv run streamlit run app.py
```
Open http://localhost:8501 in your browser to interact with regional filters and inspect the underlying data marts.


### 4. Future Roadmap & Room for Expansion
- Geospatial Analytics (DuckDB Spatial Extension): Implement spatial polygons to map exact soil sample coordinates against local weather and topography datasets.
- Automated CI/CD Workflows: Introduce GitHub Actions to run automated dbt test assertions on every pull request.
- Advanced Statistical Expectations: Expand data quality assertions using dbt-expectations to automatically flag seasonal standard deviation drifts in soil chemistry.
- Incremental Transformations: Refactor fact tables to leverage incremental materialization strategies for high-frequency IoT sensor data streams.


### 5. Bonus Section

If you feel you want to go on step further and actually collect your own soil samples to analyze. I prepared a list of affordable analytical devices, which would assist you to measure and collect data regarding your soil. Now, these devices are not nearly as advanced as NIR or Mass Spectrometers, but it will get you very far. I also just wanted to disclose that these are paid referral urls. If you are based outside of the EU, you can just search if a similar device is listed in your country of origin. Have fun and share with me any results if you get them :)


#### 5.1. Garden Tutor Soil pH Test Strips Kit

* **Price Range:** €16
* **What it measures:** Wide-range soil acidity and alkalinity (pH) using indicator strips.
* **Search Links:** [Amazon DE](https://link.amazon/B0iUpD5Q1)


#### 5.2. Atree 4-in-1 Soil Tester

* **Price Range:** €19
* **What it measures:** Digital soil pH, moisture, temperature, and environmental sunlight.
* **Search Links:** [Amazon DE](https://link.amazon/B08rWaZAP)

#### 5.3. MySoil Soil Test Kit (Mail-In Lab)

* **Price Range:** €25
* **What it measures:** Professional laboratory analysis of soil pH and major/minor macronutrients (NPK).
* **Search Links:** [Amazon DE](https://link.amazon/B09Z5sypL)

#### 5.4. Luster Leaf Rapitest Soil Test Kit

* **Price Range:** €58
* **What it measures:** Soil pH and major macronutrients (NPK) via chemical color capsules.
* **Search Links:** [Amazon DE](https://link.amazon/B04iF4ym6)


#### 5.5. LaMotte Garden Guide Soil Test Kit

* **Price Range:** €65
* **What it measures:** Professional-grade octet-comparator testing for pH, Nitrogen, Phosphorus, and Potassium.
* **Search Links:** [Amazon DE](https://link.amazon/B031I91Qw)
