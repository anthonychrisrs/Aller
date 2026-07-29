# **PROPOSAL**

## **Vision**

**Asturian Observatory (Municipal/Regional) of Demographic Intelligence** (TBC)

_"Transforming demographic data into public decisions based on scientific evidence."_

## **Mission**

To develop analytical tools and methodologies that enable the understanding, anticipation, and response to the demographic challenges of the Principality of Asturias (municipalities/regions) through data science, spatial analysis, and international evidence (optional, depending on category).

---

## **Objectives**

### **Primary Objective**

To establish a specialized consultancy in demographic intelligence to support municipalities, public administrations, NGOs, and businesses in the Principality of Asturias in the design of evidence-based public policies.

### **Secondary Objectives**

- Build a regional collaboration network.
- Participate as a technical partner in national and European projects.
- Become a regional reference in demographic analysis.
- Publish an annual report on the demographic situation in Asturias.
- Generate employment opportunities.

---

## **Problems Addressed**

| Area                | Specific Issues                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Demography**      | Aging, low birth rates, rural depopulation, urban concentration, youth emigration.                            |
| **Labor Market**    | Brain drain, professional shortages, aging workforce.                                                         |
| **Integration**     | Attraction of qualified and compatible immigrants; retention; social and labor integration; integration rate. |
| **Public Services** | Dependency, healthcare, transport, education, housing.                                                        |
| **Governance**      | Evidence-based decisions, underutilization of public data, difficulty in measuring impact.                    |

---

## **Services**

### **Level I – Data Visualization**

Includes:

- Population pyramids
- Maps
- Dashboards
- Indicators
- Descriptive reports

### **Level II – Strategic Consultancy**

Includes everything from Level I, plus:

- International benchmarking
- Simulations and scenario modeling
- Recommendations
- Policy briefs

### **Level III – Ongoing Support**

Includes:

- Impact evaluation
- Workshops
- Training
- Annual monitoring

---

## **Technical Pipeline**

### **Phase 1: Data Capture**

**Sources:**

- INE (National Statistics Institute)
- SADEI (Asturian Society of Economic and Industrial Studies)
- Eurostat
- Social Security
- Ministry of Inclusion
- Open Data Asturias
- Cadastre
- Municipal data
- Ministry of Education
- Ministry of Health

### **Phase 2: Processing & Data Governance**

- Data cleaning
- Normalization
- Integration
- **Data Privacy & Security:**
  - Anonymization and pseudonymization of sensitive records.
  - Implementation of _k-anonymity_ and _differential privacy_ techniques for public-facing datasets.
  - Strict compliance with GDPR and the Spanish LOPDGDD.

### **Phase 3: Analysis**

- Descriptive statistics
- Time series analysis
- Predictive modeling
- Spatial analysis
- International comparison
- Scenario planning

### **Phase 4: Products**

- Dashboard
- Report
- Policy brief
- Presentation
- Grant application document
- Scientific article

---

## **Main Variables**

### **Demography**

- Age, Sex, Population pyramid
- Aging index, Dependency index
- Life expectancy, Birth rate, Mortality rate
- Single-person households

### **Migration**

- Origin, Destination, Age
- Education, Occupation, Nationality
- Length of residence, Relative contribution

### **Economy**

- Employment, Unemployment, Average salary
- Social Security affiliation, Self-employed, Retirees

### **Education**

- Educational attainment, Vocational training
- University education, Continuing education

### **Health**

- Dependency, Residential care places
- Home care services, Healthcare expenditure

### **Infrastructure**

- Internet access, Transport, Housing
- Basic services

### **Innovation**

- Businesses, Startups, Patents
- R\&D, Universities

---

## **Novel Variables (Proposed)**

- **Integration Index** – employment, language, job stability, permanence, entrepreneurship.
- **Economic Contribution Index** – social security contributions, taxes, age, children, educational level.

---

## **International Benchmark**

Compare Asturias with:

- Denmark
- Finland
- Japan
- Germany
- Sweden
- Other Spanish regions / communities

---

## **Software Stack**

| Category         | Tools / Technologies                                                          |
| ---------------- | ----------------------------------------------------------------------------- |
| Data Science     | Python (Primary), DVC (Version Control)                                       |
| GIS              | QGIS (Desktop), PostGIS, GeoPandas                                            |
| Databases        | PostgreSQL + PostGIS                                                          |
| Machine Learning | Scikit-learn, XGBoost                                                         |
| Statistics       | Statsmodels, SciPy                                                            |
| Visualization    | Plotly (Interactive), Seaborn (Static), Pydeck / Kepler.gl (Advanced Spatial) |
| Dashboards       | Streamlit (Custom Apps), Metabase (BI)                                        |
| Automation       | Prefect                                                                       |
| Documentation    | MkDocs                                                                        |

---

## **Deployment & CI/CD Pipeline**

To ensure high availability, reproducibility, and continuous updates of demographic data and models:

- **Version Control**: GitLab for code repositories, DVC for models and large datasets.
- **Continuous Integration (CI)**: GitLab CI/CD pipelines to run automated testing (unit tests for data pipelines via `pytest`), linting (`ruff`), and building Docker images.
- **Continuous Deployment (CD)**: Automated deployment of Streamlit dashboards and Prefect orchestration flows triggered by GitLab CI upon merging to the main branch.
- **Infrastructure**: Containerized environments (Docker) managed via Docker Compose, ready for cloud or on-premise deployment.

---

## **Visualizations**

### **For General Public**

- Population pyramids
- Choropleth maps
- Municipal heatmaps
- Line charts
- Migration Sankey diagrams
- Traffic-light indicators
- Infographics

### **For Academic Level**

- To be defined

---

## **Potential Funding Lines**

- **LIFE Programme** – climate adaptation and territorial resilience (when environmental components are included).
- **Interreg SUDOE & Atlantic Area** – cooperation between regions with similar demographic challenges.
- **Horizon Europe – Cluster 2** (Culture, Creativity & Inclusive Society) – for public policy, governance, and social transformation.
- **Horizon Europe – Cluster 1** (Health) – if healthy aging and digital health components are included.
- **European Social Fund Plus (ESF+)** – for employment, inclusion, and integration.
- **LEADER** – for pilot projects in rural municipalities.
- **Regional Calls (Principality of Asturias)** – on innovation, demographic challenge, and digital transformation.

---

## **Project Folder Structure**

Based on the proposed software stack, the following directory structure is recommended to maintain a clean, reproducible, and scalable data science project:

```text
halfen/
├── data/
│   ├── 01_raw/            # Immutable original data (INE, Eurostat, etc.)
│   ├── 02_intermediate/   # Cleaned and normalized data
│   └── 03_processed/      # Final datasets ready for analysis & dashboards
├── models/                # Saved ML models (e.g., xgboost_integration.pkl)
├── notebooks/             # Jupyter notebooks for data exploration and prototyping
├── src/                   # Source code for the data pipelines and analysis
│   ├── __init__.py        # Makes src importable
│   ├── data_capture/      # Scripts to fetch data from APIs/web scraping
│   ├── processing/        # Data cleaning and transformation scripts
│   ├── analysis/          # Statistical and machine learning models
│   ├── flows/             # Prefect orchestration scripts
│   └── utils/             # Helper functions and common tools
├── dashboards/            # Streamlit applications and components
├── docs/                  # MkDocs documentation for the project
├── tests/                 # Unit and integration tests
├── docker/                # Dockerfiles and docker-compose (PostGIS, Metabase)
├── .env.example           # Example environment variables (secrets, DB credentials)
├── .gitignore             # Files to exclude from version control (must include data/ and models/)
├── requirements.txt       # Python dependencies (or pyproject.toml)
└── README.md              # Project overview and setup instructions
```

---

## **App Structure & User Interface**

### **1. Landing Page (Executive Summary)**

The entry point of the application, designed to give an immediate, high-level overview of the region's demographic health.

- **Hero Section:** Title (e.g., "Asturian Demographic Observatory"), brief mission statement, and a global search bar to jump directly to a specific municipality.
- **Key Performance Indicators (KPIs):** Top-level metrics with traffic-light indicators (red/yellow/green) comparing current values to the previous year or national averages:
  - Total Population & Year-over-Year Change
  - Aging Index
  - Integration Index (Overall Score)
  - Net Migration Rate
- **Interactive Regional Map:** A beautiful choropleth map of Asturias highlighting a selected metric (defaulting to Population Density or Aging Index) across municipalities. Hovering over a municipality shows a quick tooltip with its specific KPIs.
- **Recent Insights:** A section highlighting the latest automated reports, "policy briefs," or significant demographic shifts detected by the system.

### **2. Thematic Dashboards (Main Navigation Pages)**

The core of the app, divided by the main variables defined in the observatory's scope. Each page includes global filters for time (year/month) and space (region/municipality).

- **Demographics & Population:**
  - Dynamic Population Pyramids (comparing selected municipality vs. regional average).
  - Time-series charts showing birth and mortality rates over the last 20 years.
- **Migration & Integration:**
  - Sankey diagrams visualizing migration flows (Origin -> Asturias -> Destination).
  - Breakdown of the _Integration Index_ components.
- **Economy & Labor Market:**
  - Visualizations of the _Economic Contribution Index_.
  - Charts showing Social Security affiliations by age cohort and sector.
- **Health, Education & Infrastructure:**
  - Overlays of healthcare/educational facilities on a municipal map vs. population density.
  - Dependency index trends.

### **3. Advanced Tools & Academic View**

Dedicated sections for Level II/III services and technical users.

- **Data Explorer:** A tabular view allowing users to select multiple variables, filter by municipality, and export datasets to CSV/Excel.
- **Scenario Modeler (Simulations):** Interactive tool where users can adjust sliders (e.g., "What if net migration increases by 10%?") to see projected impacts on the population pyramid and aging index over the next 10-20 years.
- **Benchmarking Tool:** Side-by-side comparison of Asturian metrics against the international benchmark regions (Denmark, Finland, Japan, etc.).
