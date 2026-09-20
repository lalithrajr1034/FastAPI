from fastapi import FastAPI, HTTPException, Path, Query
from data import Data


products = Data()
app = FastAPI()


# by this httpexception we can raise the http error's accordingly because in some side error raising is not been done 

@app.get('/category/{cate}')
def categories(cate:str = Path(..., description='This is the product category', example='electronics')):
    li = []
    for product in products:
        if product['category'] == cate:
            li.append(product)
    if li:
        return li
    else:
        raise HTTPException(status_code=404, detail=f'product of ** {cate} ** not found')