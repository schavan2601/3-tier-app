FROM postgres:13
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
COPY ./app/init.sql /docker-entrypoint-initdb.d/
RUN pip install -r requirements.txt
COPY ./app/ .
CMD ["python", "main.py"]