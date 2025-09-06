from flask import Flask
from prometheus_client import start_http_server, Summary, Counter


app = Flask(__name__)

# Prometheus Metrics
REQUEST_TIME = Summary('request_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_total', 'Total HTTP GET requests')


@app.route('/')
@REQUEST_TIME.time()
def hello():
    REQUEST_COUNT.inc()
    return 'Hello, World!'


@app.route('/health')
def health():
    REQUEST_COUNT.inc()
    return "OK", 200


if __name__ == "__main__":
    # Startup prometheus server
    start_http_server(8000)

    app.run(host="0.0.0.0", port=5000, debug=False)
