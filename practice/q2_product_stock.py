from fastapi import FastAPI, Query, Path, HTTPException
from pd import data
# GET /products/{product_id}/stock

data = data()
app = FastAPI()

@app.get('/products/{product_id}/stock')
def product_quantity(product_id:int = Path(..., description='information code of a product', example='100'),
                    quantity:int = Query(..., gt=0)):
    product = [prod for prod in data if prod['product_id'] == product_id]
    if not product:
        raise HTTPException(status_code= 404, detail='product not fount')
    if product[0]['stock']<quantity:
        raise HTTPException(status_code=400, detail='quantity is not available')
    
    return {'product':product[0], 'av_quantity':product[0]['stock'],'req_quantity':quantity}