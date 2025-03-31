from celery import Celery

CELERY_BROKER_URL = "pyamqp://guest@localhost//"
BACKEND_URL = "redis://localhost"

app = Celery(__name__, broker=CELERY_BROKER_URL)


@app.task
def add(x, y):
    return x + y