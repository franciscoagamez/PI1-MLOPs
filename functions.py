import pandas as pd
import os

"""
def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

"""
def PlayTimeGenre(genero: str):
    result_df = pd.read_csv('data/DataAPI/PlayTimeGenre.csv')

    # Filtrar el DataFrame para el género específico
    filtered_df = result_df[result_df['genres'] == genero]
    
    # Agrupar por año de lanzamiento y sumar las horas jugadas
    grouped_df = filtered_df.groupby('year')['hours_game'].sum()
    
    # Encontrar el año con más horas jugadas
    max_hours_year = grouped_df.idxmax()

    # Construye el response_data
    response_data = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_hours_year)}

    # Muestra el resultado
    return response_data

"""
def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas 
para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: 
{"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, 
                                                {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

"""

def UserForGenre(genero:str):
    consulta2 = pd.read_csv('data/DataAPI/UserForGenre.csv')
    
    # Filtrar el DataFrame por el género dado
    genre_data = consulta2[consulta2['genres'] == genero]

    # Encontrar al usuario con más horas jugadas para ese género
    top_user = genre_data.loc[genre_data['hours_game'].idxmax()]['user_id']

    # Crear una lista de acumulación de horas jugadas por año
    hours_by_year = genre_data.groupby('year')['hours_game'].sum().reset_index()
  
    hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
    
    hours_list = hours_by_year.to_dict(orient='records')

    # Crear el diccionario de retorno
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }

    return result

"""
def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

"""

def UsersRecommend(year: int):
    df = pd.read_csv("data/DataAPI/UsersRecommend.csv")
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]

    response_data = [{"Puesto 1": result_df.iloc[0]['title']},
                     {"Puesto 2": result_df.iloc[1]['title']},
                     {"Puesto 3": result_df.iloc[2]['title']}]

    return response_data

"""
def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

"""

def UsersNotRecommend(year: int):
    df = pd.read_csv('data/DataAPI/UsersNotRecommend.csv')

    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]
    
    response_data = [{"Puesto 1": result_df.iloc[0]['title']},
                    {"Puesto 2": result_df.iloc[1]['title']},
                    {"Puesto 3": result_df.iloc[2]['title']}]
    
    return response_data

"""
def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

"""

def sentiment_analysis(year: int):
    df = pd.read_csv('data/DataAPI/sentiment_analysis.csv')

    # Filtrar por la empresa desarrolladora
    result_df = df[df['Year'] == year]

    # Convertir a formato de diccionario
    response_data = result_df.set_index('Year').to_dict(orient='index')
    
    return response_data
"""
def recomendacion_juego( id de producto ): Ingresando el id de producto, 
deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

"""

def recomendacion_juego(item_id):
    df = pd.read_csv('data/DataML/modelo_item_item.csv')
    
    # Filtrar el DataFrame por el input
    result_df = df[df['item_id'] == item_id]
    
    response_data = result_df[["title","Recomendados"]]
 
    return response_data