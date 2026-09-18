from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/a")
def hi():
    return 'hi'

@app.get("/aa/{value}")
def hello(value:int = Path(...,title='this is title', gt = 0)):
    return value

@app.get("/products")
def products(limit: int):
    return {"limit": limit}