FROM apache/airflow:2.7.3

USER root
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
