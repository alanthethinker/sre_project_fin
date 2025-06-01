from fastapi import FastAPI, Query
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/add")
def add(a: int = Query(...), b: int = Query(...)):
    return {"result": a + b}

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)
