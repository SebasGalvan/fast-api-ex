from typing import Union
from fastapi import FastAPI

from  models.item_model import Item


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

# http://127.0.0.1:8000/calculadora?parm1=6&parm2=7
@app.get('/calculadora')
def calculadora(parm1: int, parm2 : int):
    return {'suma': parm1 + parm2}

@app.put('/item/{item_id}')
def update_item(item_id : int, item : Item):
    return {'item_name': item.name, 'item_id' : item_id}
    ...
# Activar entorno
# Para ejecutar el programa: uvicorn main:app --reload


# Modelos



    