
# Necesitaremos `pandas` así que  vamos a impórtalo.

import pandas as pd

# Leeremos el archivo `music_project_en.csv` de la carpeta  y lo  guárdamos en la variable `df`:

df = pd.read_csv('music_project_en.csv')

print(df.describe())

# Imprimimos las 10 primeras filas de la tabla:
print(df.head(10))

# Obtenemos la información general sobre la tabla con un comando:

print(df.info())

# Correguimos el formato en los encabezados de las columnas y ocúpate de los valores ausentes. Después, compruebaremos si hay duplicados en los datos.

df.columns

# Cambiamos los nombres de las columnas de acuerdo con las reglas del buen estilo:
# * Si el nombre tiene varias palabras, utilizaremos snake_case
# * Todos los caracteres deberan ser minúsculas
# * Eliminaremos los espacios

df.rename(columns={
    '  userID': 'user_id',
    'Track': 'track',
    '  City  ': 'city',
    'Day': 'day'}, inplace=True)
# Comprobamos el resultado. Imprimiendo los nombres de las columnas una vez más:

print(df.columns)


# ### Valores ausentes <a id='missing_values'></a>
# Lo primero encontrar el número de valores ausentes en la tabla. Para ello, utilizaremos dos métodos pandas:
print(df.isna().sum())
# Reemplazaremos los valores ausentes en `'track'`, `'artist'`, y `'genre'` con la string `'unknown'`. Para ello, creamos la lista `columns_to_replace`,  vamos a recórrerla con un bucle `for`  reemplazando
#  los valores ausentes en cada una de las columnas:
columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')
# Asegúrandonos asi que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

print(df.isna().sum())

# ### Duplicados <a id='duplicates'></a>
# Hallamos el número de duplicados obvios en la tabla utilizando un comando:
print(df.duplicated().sum())

# Llamamos al método `pandas` para deshacerte de los duplicados obvios:
df.drop_duplicates(inplace=True)

# Contamos de nuevo los duplicados obvios para asegurarte de que todos han sido eliminados:

print(df.duplicated().sum())

# Ahora nos vamos ha  deshacer de los duplicados implícitos en la columna genre. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar a resultado. Poe ello es importante realizar este proceso.

print(df['genre'].sort_values().unique())

# Inpeccionamos  la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.

# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` con el valor en `correct_genre`.


def replace_wrong_genres(wrong_genres, correct_genre):
    df['genre'] = df['genre'].replace(wrong_genres, correct_genre)

# Llamamos a `replace_wrong_genres()` y le pasamos argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:


wrong_genres = ['hip', 'hop', 'hip-hop']
correct_genre = 'hiphop'

replace_wrong_genres(wrong_genres, correct_genre)

print(df['genre'].sort_values().unique())

# ### Conclusiones <a id='data_preprocessing_conclusions'></a>

# Evaluemos la actividad del usuario en cada ciudad. Para esto Agruparemos los datos por ciudad encontrando de esta forma el número de canciones reproducidas en cada grupo.
print(df.groupby('city')['user_id'].count())

# Ahora agrupemos los datos por día de la semana y encuentramos el número de pistas reproducidas el lunes, miércoles y viernes.

print(df.groupby('day')['user_id'].count())

# Apliquemos un filtrado consecutivo con indexación lógica.
# Después, calculamos los valores de la columna `'user_id'` en la tabla resultante. Almacenamos el resultado en la nueva variable. Recuperaremos esta variable de la función.


def number_tracks(day, city):
    track_list = df.loc[df['day'] == day]
    track_list = track_list.loc[track_list['city'] == city]
    return track_list['user_id'].count()


number_tracks(day='Monday', city='Springfield')

number_tracks(day='Monday', city='Shelbyville')

number_tracks(day='Wednesday', city='Springfield')

number_tracks(day='Wednesday', city='Shelbyville')

number_tracks(day='Friday', city='Springfield')

number_tracks(day='Friday', city='Shelbyville')

# Utilizamos un `pd.DataFrame` para crear una tabla, donde
# * Los nombres de las columnas son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que conseguiste de `number_tracks()`

data_mod = pd.DataFrame({
    'city': ['Springfield', 'Shelbyville'],
    'monday': [15740, 5614],
    'wednesday': [11056, 7003],
    'friday': [15945, 5895]})

print(data_mod)

# **Conclusiones**
#
# Los datos revelan las diferencias en el comportamiento de los usuarios:
#
# - En Springfield, el número de canciones reproducidas alcanzan el punto máximo los lunes y viernes mientras que los miércoles hay un descenso de la actividad.
# - En Shelbyville, al contario, los usuarios escuchan más música los miércoles. La actividad de los usuarios los lunes y viernes es menor.

spr_general = df.loc[df['city'] == 'Springfield']
shel_general = df.loc[df['city'] == 'Shelbyville']

print(shel_general)

# La función debería devolver información de los 15 géneros más populares de un día determinado en un período entre dos marcas de fecha y hora.


def genre_weekday(df, day, time1, time2):

    df_tmp = df.loc[df['day'] == day]
    df_tmp = df_tmp.loc[df_tmp['time'] > time1]
    df_tmp = df_tmp.loc[df_tmp['time'] < time2]
    return df_tmp.groupby('genre')['user_id'].count().sort_values(ascending=False)[:15]


genre_weekday(df, 'Monday', '07:00', '11:00')

genre_weekday(spr_general, 'Monday', '07:00', '11:00')

genre_weekday(shel_general, 'Monday', '07:00', '11:00')

genre_weekday(spr_general, 'Friday', '17:00', '23:00')

genre_weekday(shel_general, 'Friday', '17:00', '23:00')

# Agrupamos la tabla `spr_general` por género y encontramos el número de canciones reproducidas de cada género con el método `count()`. Después, ordenaremos el resultado en orden descendente y lo guárdamos en `spr_genres`.

spr_genres = spr_general.groupby(
    'genre')['genre'].count().sort_values(ascending=False)

print(spr_genres.head(10))

# Ahora hacemos lo mismo con los datos de Shelbyville.
# Agrupamos la tabla `shel_general` por género y encontramos el número de canciones reproducidas de cada género. Después, ordenaremos el resultado en orden descendente y  lo guárdamos en la tabla `shel_genres`:
shel_genres = shel_general.groupby(
    'genre')['genre'].count().sort_values(ascending=False)

# Se imprimen las 10 primeras filas de `shel_genres`:

print(shel_genres[:10])


# # Conclusiones <a id='end'></a>
# Hemos probado las siguientes tres hipótesis:
#
# 1. La actividad de los usuarios difiere dependiendo del día de la semana y de las distintas ciudades.
# 2. Los lunes por la mañana los residentes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen distintas preferencias. En ambas ciudades, Springfield y Shelbyville, se prefiere el pop.
#
# Tras analizar los datos, concluimos:
#
# 1. La actividad del usuario en Springfield y Shelbyville depende del día de la semana aunque las ciudades varían de diferentes formas.
#
# La primera hipótesis ha sido aceptada completamente.
#
# 2. Las preferencias musicales no varían significativamente en el transcurso de la semana en Springfield y Shelbyville. Podemos observar pequeñas diferencias en el orden los lunes, pero:
# * En Springfield y Shelbyville la gente lo que más escucha es la música pop.
#
# Así que no podemos aceptar esta hipótesis. También debemos tener en cuenta que el resultado podría haber sido diferente si no fuera por los valores ausentes.
#
# 3. Resulta que las preferencias musicales de los usuarios de Springfield y Shelbyville son bastante parecidas.
#
# La tercera hipótesis es rechazada. Si hay alguna diferencia en las preferencias no se puede observar en los datos.
