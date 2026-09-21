from fastapi import FastAPI, Query, Path, HTTPException
from pd import data


data = data()
app = FastAPI()


@app.get('products/category')
def categoryes():
    return data
