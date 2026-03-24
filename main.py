from fastapi import FastAPI

app = FastAPI()


@app.get("/sum/{a}/{b}")
def sum_numbers(a: int, b: int):
    return {"result": a + b}