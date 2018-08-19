# Series(collections of values)
# DataFrame(collections of Series objects)

import pandas as pd
from pandas import Series
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
# print(series_film)
print(type(series_film))
film_name = series_film.values
print(type(film_name))

series_tomatoes = fandango['RottenTomatoes']
series_custom = Series(series_tomatoes.values,index=film_name)
print(series_custom)