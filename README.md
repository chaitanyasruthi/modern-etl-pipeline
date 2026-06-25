# Modern ETL Pipeline

## Overview

This project implements a Modern ETL Pipeline using:

- Apache Spark
- Apache Airflow
- PostgreSQL
- MinIO
- Docker
- Streamlit

---

## Architecture

```
Generate Data
      │
      ▼
Bronze (MinIO)
      │
      ▼
Spark Bronze → Silver
      │
      ▼
Silver Parquet
      │
      ▼
Spark Silver → Gold
      │
      ▼
PostgreSQL
      │
      ▼
Streamlit Dashboard
```

---

## Technologies

- Python
- Apache Spark
- Airflow
- PostgreSQL
- MinIO
- Docker
- Streamlit

---

## Project Structure

```
modern-etl-pipeline/

├── dags/
├── jobs/
│   ├── generate_data.py
│   ├── bronze_to_silver.py
│   ├── silver_to_gold.py
│   └── load_to_postgres.py
│
├── streamlit/
│   └── app.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

## Run

Start Docker:

```bash
docker compose up -d
```

Generate data:

```bash
python jobs/generate_data.py
```

Run Spark:

```bash
spark-submit jobs/bronze_to_silver.py
```

Load Gold metrics:

```bash
python jobs/load_to_postgres.py
```

Start Dashboard:

```bash
streamlit run streamlit/app.py
```

---

## Output

- Bronze data stored in MinIO
- Silver data stored as Parquet
- Gold metrics stored in PostgreSQL
- Dashboard built with Streamlit