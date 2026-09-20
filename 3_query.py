from fastapi import FastAPI, Query, HTTPException
from data import Data


app = FastAPI()
dataset = Data()

# Validates input: checks values in the URL (e.g. limit between 1 and 100, search text at least 3 characters)
# Protects the server: blocks bad or huge requests automatically with a 422 error
# Saves code: no need to write manual if checks
# Improves docs: rules show up in /docs automatically
# Cleaner URLs: alias lets you use names like item-query in the URL


""" here we are getting the products in sorted manner with respect to categories"""
#?sort=asc&cat=electronics

@app.get('/')
def items(sort:str = Query('desc', description='Here we are getting the products in sorted manner', max_length=4, min_length=3),
          cat:str = Query(..., description= 'categoris of products', example='accessories')):
    categories = ["electronics", "accessories", "audio"]
    sorting = ['asc', 'desc']
    
    if sort not in sorting:
        raise HTTPException(status_code=400, detail='Your entered sorting order value is not proper')
    if cat not in categories:
        raise HTTPException(status_code=400, detail=f'category ** {cat} **  not fount in the data base')
    
    bool_ = True if sort=='desc' else False
    
    sorted_desc = sorted(dataset, key=lambda p: p["price"], reverse=bool_)
    return [p for p in sorted_desc if p['category'] == cat]
    