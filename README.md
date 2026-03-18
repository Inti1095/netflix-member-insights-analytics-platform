# Netflix Member Insights Analytics Platform

## 🏗️ Architecture Overview

```
Data Source (Simulated Streaming Events)
        ↓
Ingestion Layer (Python)
        ↓
Data Lake (Parquet)
        ↓
PySpark ETL (Clean + Transform)
        ↓
dbt Models (Metrics Layer)
        ↓
Airflow DAG (Orchestration)
        ↓
Analytics Warehouse (Postgres/BigQuery)
        ↓
Dashboards (Tableau / Looker / Streamlit)
```

## Tech Stack
- Ingestion: Python + Pandas
- Data Lake: Parquet files
- ETL: PySpark
- Data Modeling: dbt
- Orchestration: Apache Airflow
- Warehouse: PostgreSQL
- Visualizations: Streamlit
