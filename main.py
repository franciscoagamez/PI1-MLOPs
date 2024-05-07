#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, HTTPException 
import traceback  # Importa la biblioteca para imprimir la traza de la pila
from typing import List, Dict
import pandas as pd
#import pyarrow
from functions import UsersRecommend
from functions import sentiment_analysis
from functions import UsersNotRecommend
from functions import PlayTimeGenre
from functions import UserForGenre
from functions import recomendacion_juego
#from modelo_item_item import recomendacion_usuario


# In[ ]:


# Crea una instancia de la aplicación FastAPI
app = FastAPI()


# In[ ]:

@app.get("/")
async def root():
    return {"Mensaje": "Proyecto Individual"}

# In[ ]:


@app.get("/PlayTimeGenre/{genero}")
async def user(genero: str):
    try:
        result = PlayTimeGenre(genero)
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")

    except Exception as e:
        traceback.print_exc()  # Imprime la traza de la pila
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# In[ ]:   

@app.get("/UserForGenre/{genero}")
async def user(genero: str):
    try:
        result = UserForGenre(genero)
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")

    except Exception as e:
        traceback.print_exc()  # Imprime la traza de la pila
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# In[ ]:

@app.get("/UsersRecommend/{year}")
async def user(year: int):
    try:
        year = int(year)
        
        result = UsersRecommend(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")
# In[ ]:

@app.get("/UsersNotRecommend/{year}")
async def user(year: int):
    try:
        year = int(year)

        result = UsersNotRecommend(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersNotRecommend.csv: {str(e)}")
    

@app.get("/sentiment_analysis/{year}")
async def user(year: int):
    try:
        result = sentiment_analysis(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")


@app.get("/recomendacion_juego/{item_id}", tags=['recomendacion_juego item_item'])
async def item(item_id: int):

    try:
        item_id = int(item_id) 
        result = recomendacion_juego(item_id)
        
        return result
    
    except Exception as e:
        return {"error":str(e)}