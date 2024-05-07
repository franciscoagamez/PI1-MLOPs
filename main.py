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



# In[ ]:


# Crea una instancia de la aplicación FastAPI
app = FastAPI()

#class Item(BaseModel)
    


@app.get("/PlayTimeGenre/{genero}", tags=['Endpoints'],
         summary="Debe devolver año con mas horas jugadas para dicho género.",
         description="Algunos de los géneros que puedes ingresar como ejemplo: Action, Adventure, Casual, Indie")
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

@app.get("/UserForGenre/{genero}",tags=['Endpoints'],
         summary="Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.",
         description="Algunos de los géneros que puedes ingresar como ejemplo: Action, Adventure, Casual, Indie, Simulation, Strategy")
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

@app.get("/UsersRecommend/{year}",tags=['Endpoints'],
         summary="Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.",
         description="Escriba años entre 2010 - 2015")
async def user(year: int):
    try:
        year = int(year)
        
        result = UsersRecommend(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")
# In[ ]:

@app.get("/UsersNotRecommend/{year}",tags=['Endpoints'],
         summary="Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado",
         description="Escriba años entre 2010 - 2015")
async def user(year: int):
    try:
        year = int(year)

        result = UsersNotRecommend(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersNotRecommend.csv: {str(e)}")
    

@app.get("/sentiment_analysis/{year}",tags=['Endpoints'],
         summary="Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.",
         description="Puede insertar años entre 1989 hasta 2017")
async def user(year: int):
    try:
        result = sentiment_analysis(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")


@app.get("/recomendacion_juego/{item_id}", tags=['Modelo de recomendacion de video juegos item-item'],
         summary="Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.",
         description="Algunos ids de ejemplo: 761140, 643980, 670290, 772540, 658870, 733530")
async def item(item_id: int):

    try:
        item_id = int(item_id) 
        result = recomendacion_juego(item_id)
        
        return result
    
    except Exception as e:
        return {"error":str(e)}