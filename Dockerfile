FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/pimik09-droid/devops-junior-project"
LABEL org.opencontainers.image.description="DevOps Junior Project Flask application"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]