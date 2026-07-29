# Demo Website Specification: Asturian Observatory of Demographic Intelligence

## 1. Introduction

This document outlines the specifications for the initial website demo (MVP) of the **Asturian Observatory of Demographic Intelligence**. The demo will be built using **Streamlit** (as per the proposed software stack) to showcase the core analytical capabilities, interactive visualizations, and evidence-based policy tools to potential stakeholders (municipalities, NGOs, and regional administration).

## 2. Target Audience for the Demo

- Municipal policymakers (Mayors, Councilors, Technicians)
- Regional administration officials
- Grant evaluators and funding bodies (e.g., Horizon Europe, LEADER, LIFE)

## 3. Demo Architecture & Stack

- **Web Framework**: Streamlit (Python)
- **Geospatial Visualization**: Pydeck / Kepler.gl (for interactive Choropleth and Heatmaps)
- **Charts & Graphs**: Plotly (Interactive Population Pyramids, Sankey diagrams, Time-series)
- **Data Source**: Local processed datasets (Parquet/CSV format) located in `data/03_processed/`, mimicking integrated data from INE, SADEI, and Social Security.

## 4. Website Structure (Streamlit Multi-page App)

The demo will be structured with a side navigation bar linking to four main pages, progressing from descriptive statistics to predictive policy tools.

### Page 1: Home (Executive Summary & Dashboards)

- **Hero Section**: Vision and Mission statement.
- **Global KPI Traffic Lights**:
  - Current Total Population (Asturias vs. National Average).
  - Aging Index & Dependency Index.
  - Proposed _Integration Index_ (Regional average).
- **Key Visual**: An interactive 3D municipal heatmap (using Pydeck) showing demographic urgency (e.g., severe depopulation zones in red).

### Page 2: Demographic Insights (Level I Service - Data Visualization)

- **Sidebar Filters**:
  - Select Municipality (e.g., Oviedo, Gijón, Tineo, Cangas del Narcea — offering a mix of urban and rural profiles).
  - Select Year range.
- **Visualizations**:
  - _Interactive Population Pyramid_: Overlaying the selected municipality's pyramid against the overall Asturian or International benchmark (e.g., Denmark or Finland).
  - _Time-series Line Chart_: Birth rates vs. Mortality rates over the last 20 years.
  - _Vulnerability Metrics_: Bar charts highlighting single-person households and elderly dependency ratios.

### Page 3: Migration, Integration & Labor Market

- **Sidebar Filters**: Employment Sector, Demographic Origin/Destination.
- **Visualizations**:
  - _Sankey Diagram_: Visualizing migration flows (e.g., Rural -> Urban, External -> Asturias, Asturias -> Madrid/Abroad).
  - _Novel Index Dashboards_:
    - **Integration Index**: Radar chart breaking down employment, language, job stability, and permanence for incoming populations.
    - **Economic Contribution Index**: Scatter plot analyzing the correlation between age, educational level, and social security contributions.

### Page 4: Policy Simulator (Level II Service - Strategic Consultancy)

- **Concept**: A preview of the scenario modeling capability to aid public governance.
- **Interactive Controls (Sliders & Toggles)**:
  - _Scenario A_: "What if we increase the youth retention rate by X%?"
  - _Scenario B_: "What if we attract X highly qualified professionals to a specific rural municipality?"
- **Output**: Real-time predictive charts showing the simulated impact on the Dependency Index, local tax revenue projections, and public service demand (e.g., healthcare, schools) over the next 5 to 15 years.

## 5. Mock Data Requirements for Demo

To build this demo without exposing sensitive or raw data, the following datasets will need to be synthesized or aggregated:

1. `municipal_demographics_mock.parquet`: Age, sex, population by municipality (2000-2025).
2. `migration_flows_mock.csv`: Origin, destination, age group, employment sector flows.
3. `custom_indices_mock.csv`: Synthetic dataset calculating the Integration and Economic Contribution indices for key municipalities.

## 6. Next Steps for Demo Deployment

1. Initialize the `halfen/` project structure.
2. Generate and store synthetic data in `data/03_processed/`.
3. Develop Streamlit components in the `dashboards/` directory.
4. Containerize the application using `docker/Dockerfile`.
5. Deploy the demo (via Streamlit Community Cloud or an internal testing server) for stakeholder review and feedback.
