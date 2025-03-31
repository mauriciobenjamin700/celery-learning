from celery import Celery
from time import sleep

BROKER_URL = "redis://localhost:6379"

app = Celery("tasks", broker=BROKER_URL, backend=BROKER_URL)


@app.task
def process(x: int, y: int) -> int:
    """
    A simple task that adds two numbers three times.
    
    This is a Celery task that takes two integers, adds them together, and returns the result.
    """
    
    i = 0
    result = 0
    
    while i < 3:
        sleep(1)
        result = x + y
        i += 1
        print(f"Processing: X -> {x} and Y -> {y} then result -> {result}")
        
    return result