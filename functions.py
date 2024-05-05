import pandas as pd
import os



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


def UsersRecommend(year: int):
    df = pd.read_csv("data/DataAPI/UsersRecommend.csv")
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]

    response_data = [{"Puesto 1": result_df.iloc[0]['title']},
                     {"Puesto 2": result_df.iloc[1]['title']},
                     {"Puesto 3": result_df.iloc[2]['title']}]

    return response_data

def UsersNotRecommend(year: int):
    df = pd.read_csv('data/DataAPI/UsersNotRecommend.csv')

    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]
    
    response_data = [{"Puesto 1": result_df.iloc[0]['title']},
                    {"Puesto 2": result_df.iloc[1]['title']},
                    {"Puesto 3": result_df.iloc[2]['title']}]
    
    return response_data

def sentiment_analysis(year: int):
    df = pd.read_csv('data/DataAPI/sentiment_analysis.csv')

    # Filtrar por la empresa desarrolladora
    result_df = df[df['Year'] == year]

    # Convertir a formato de diccionario
    response_data = result_df.set_index('Year').to_dict(orient='index')
    
    return response_data