from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests received by the application",
    ["endpoint"],
)


@app.route("/")
def index():
    REQUEST_COUNT.labels(endpoint="/").inc()

    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Junior Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 760px;
                margin: 60px auto;
                padding: 0 24px;
                line-height: 1.6;
                color: #1f2937;
            }
            h1 {
                color: #2563eb;
            }
            code {
                background: #f3f4f6;
                padding: 2px 6px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1>Привет! Это мой DevOps-проект</h1>
        <p>Приложение запущено в Docker-контейнере.</p>
        <p>Проверка здоровья: <code>/health</code></p>
        <p>Метрики Prometheus: <code>/metrics</code></p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return {"status": "ok"}, 200


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
