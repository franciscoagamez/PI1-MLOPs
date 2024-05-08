![Texto alternativo](assets/PresentacionSteam.jpg)


# Machine Learning Operations (MLOps).

## Sistema de Recomendación de Videojuegos para Usuarios de Steam

### Introducción:

El presente proyecto hace parte de la etapa de labs del bootcamp de Henry, cuyo objeto consiste en tomar un caso real y aplicar los conocimientos aprendidos a lo largo de los diferentes módulos. 

### Objetivo del proyecto:

El objetivo de este proyecto fue el de asumir el rol de Data Scientist en Steam, una plataforma multinacional de videojuegos sobre la cual se debía desarrollar todo un flujo de trabajo, abordando los procesos de ETL (Extracción, Transformación y Carga), EDA (Análisis exploratorio de los datos) y disponibilización de los datos mediante la creación de un API con 6 funciones principales. 

Dos de las funciones mencionadas, disponibilizan un modelo de ML (Machine Learning) que contienen, por un lado, análisis de sentimientos aplicados a los reviews de los comentarios extraídos de uno de los datasets (def sentiment_analysis) y la otra función (def recomendacion_juego) utiliza el modelo matemático de la similitud del coseno, para recomendar mediante el ingreso del id de un video juego, 5 relacionados.

### Funciones Desarrolladas para la API:

Las siguientes son als funciones para los endpoints que se consumirán en la API.

- def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

- def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

- def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

- def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

- def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

- def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

### Herramientas y librerías utilizadas: 

Python, Pandas, Scikit-Learn, FastAPI, Uvicorn, Render, Matplotlib, Seaborn, Plotly, WordCloud, Numpy, NLTK.

### Enlaces de interés:

1. [Despliegue de la API en Render ](https://pi1-mlops-ew6o.onrender.com/)
2. [Video Explicativo del proceso (youtube) ](https://youtu.be/W_x8cJtv-jc)
3. [Datasets usados y diccionario de datos ](https://drive.google.com/drive/folders/1H5C77FkcfqbtCTbPYQLWuT1mkuLT5TWO?usp=drive_link)
4.  [Repositorio de GitHub](https://github.com/franciscoagamez/PI1-MLOPs)
5. [Mi perfil de Linkedin ](https://www.linkedin.com/in/francisco-ag%C3%A1mez-bb132857)

Gracias por tomarte el tiempo para mirar este repositorio. En caso de que consideres pertinente realizar un aporte o mejora no dudes en contactarme a través de mi LinkedIn :)

Desarrollado por Francisco Javier Agámez G.
