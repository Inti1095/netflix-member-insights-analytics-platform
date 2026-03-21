# 🎬 Netflix Member Insights Analytics Platform

## 🚀 Overview

This project is a **production-style end-to-end data analytics platform** designed to simulate how companies like Netflix analyze user engagement at scale.

It demonstrates the full lifecycle of data:

**Ingestion → Processing → Analytics → Orchestration → Visualization → Data Quality**

---

## 🎯 Problem Statement

Streaming platforms must process millions of user events daily to understand:

- User engagement
- Content performance
- Retention behavior

This project simulates that environment by generating **1M+ events/day** and transforming them into actionable insights such as:

- Daily Active Users (DAU)
- Total Watch Time
- User Interaction Trends

---

## 🏗️ Architecture


            +----------------------+
            |   Airflow (DAG)      |
            | Orchestration Layer  |
            +----------+-----------+
                       |
                       v
    +------------------+------------------+
    |                                     |
    v                                     v

    +---------------+ +----------------+
| Ingestion | | ETL (Spark) |
| Python Script | | Transformation |
+-------+-------+ +--------+-------+
| |
v v
data/raw/ data/processed/
| |
+---------------+--------------------+
|
v
+------------------+
| dbt Models |
| Metrics Layer |
+--------+---------+
|
v
+------------------+
| Dashboard |
| (Streamlit) |
+------------------+
|
v
+------------------+
| Data Quality |
| Tests (PyTest) |
+------------------+


---

## ⚙️ Tech Stack

- **Python** → Data ingestion & scripting  
- **PySpark** → Distributed data processing  
- **dbt** → Analytics & metrics modeling  
- **Airflow** → Workflow orchestration  
- **Streamlit** → Dashboard visualization  
- **Pandas** → Data analysis  
- **PyTest** → Data quality testing  

---

## 📊 Key Metrics

The platform computes:

- **DAU (Daily Active Users)**
- **Total Watch Time**
- **Total Events**
- **User Engagement Trends**

---

## 📁 Project Structure

netflix-member-insights-analytics-platform/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── ingestion/
│ └── generate_events.py
│
├── etl/
│ └── pyspark_etl.py
│
├── dbt/
│ └── models/marts/metrics.sql
│
├── airflow/
│ └── dags/pipeline_dag.py
│
├── dashboards/
│ └── streamlit_app.py
│
├── tests/
│ └── test_data_quality.py
│
└── README.md



---

## 🔄 Pipeline Flow

1. **Ingestion**
   - Simulates 1M user events
   - Writes JSON data to `data/raw/`

2. **ETL (PySpark)**
   - Cleans and transforms raw data
   - Outputs to `data/processed/`

3. **Analytics (dbt)**
   - Builds metrics like DAU and engagement

4. **Orchestration (Airflow)**
   - Automates pipeline execution

5. **Dashboard (Streamlit)**
   - Visualizes user behavior

6. **Data Quality Tests**
   - Ensures no null user IDs

---

## 🚀 How to Run

### 1. Generate Data
```bash
python ingestion/generate_events.py
