# Aprendendo mais sobre Celery

- [doc oficial](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

Dado o seguinte código:

```python
from celery import Celery
from time import sleep

BROKER_URL = "redis://localhost:6379"

app = Celery("tasks", broker=BROKER_URL)


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
```

o nome do arquivo onde as tasks ficam deve ser informado para o celery

Quando a função `process` é chamada, ela vai ser executa em primeiro plano, desta forma `process(1,2)`. Agora se chamarmos a mesma função desta forma `process.delay(1,2)` ela será executada em segundo plano pelo celery.

## Dicas

- Acesse seus scripts python de forma interativa usando `python -i seu_arquivo.py`
- Inicie o celery usando `celery -A tasks worker -l info`, onde tasks é o arquivo.py com as tarefas a serem executadas.

## Referencias usadas

- [Introdução ao Celery: Tarefas assíncronas em Python](https://www.youtube.com/watch?v=VRHVEporra0)
