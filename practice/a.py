from fastapi import FastAPI, Query, Path, HTTPException
from pd import data


data = data()
app = FastAPI()

@app.get('/products/{product_id}')
def product(product_id:int = Path(..., description='id of a product'),
            discount:int = Query(..., ge=0, le=100)):
    
    # railse the error and get the data info
    prod = [prod for prod in data if prod['product_id'] == product_id]
    if not prod:
        raise HTTPException(status_code=404, detail='user data is not vailable')
    
    dis_price = prod[0]["price"] - (prod[0]["price"]*discount/100)
    return {'Product info':prod[0],'Final Price':dis_price}

