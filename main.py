from typing import Union
from fastapi import FastAPI

#Creacion de una app FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get('/hola')
def read_home():
    return {'Hello':'from home'}

@app.get('/items/{item_id}')
def read_item(item_id : int, q : Union[str, None] = None):
    return {'item_id' : item_id, 'q' : q} 


@app.get('/items')
def get_items():
    return {'items' : 'all items'}


# Para ejecutar el programa: uvicorn main:app --reload