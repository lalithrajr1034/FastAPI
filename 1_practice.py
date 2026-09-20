from fastapi import FastAPI, Path, Query
from data import Data


app = FastAPI()

@app.get("/a")
def hi():
    return 'hi'

@app.get("/product_search/{p_id}")
def hello(p_id:int = Path(...,description='this is product id', example=10, gt = 0)):
    data = Data()
    
    for product in data:
        if product['id'] == p_id:
            return product
    if True:
        return {'mesage' :'product is not there'}