# Real-Time CSV to PostgreSQL Pipeline using Apache Airflow

This project demonstrates an end-to-end ETL pipeline where CSV files are loaded into a PostgreSQL database using Apache Airflow. The entire pipeline is containerized with Docker and can be orchestrated using Airflow's scheduler.

## 📌 Features

- Dockerized environment with Airflow and PostgreSQL
- Automated DAG for CSV ingestion
- PostgresHook for seamless SQLAlchemy integration
- Scalable architecture with volume mapping
- Easy-to-use setup with `docker-compose`

## 🏗️ Architecture

## 🧰 Tech Stack

- Python 3.8+
- Apache Airflow 2.8
- PostgreSQL 13
- Docker & Docker Compose
- Pandas
- SQLAlchemy

---

## 📁 Project Structure

csv_to_postgres_airflow/
├── dags/
│ └── csv_to_postgres_dag.py
├── data/
│ └── your_data.csv
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/csv_to_postgres_airflow.git
cd csv_to_postgres_airflow


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt



docker-compose up --build
