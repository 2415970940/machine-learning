import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fandango = pd.read_csv('fandango_score_comparison.csv')
cols = ['FILM','RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
rows =fandango[cols]
print(rows[:1])

num_clos = ['RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
score = fandango[num_clos]
values = score.ix[0,num_clos].values
print(values)
bar_position = np.arange(4)+0.75

fig,ax = plt.subplots()
ax.bar(bar_position,values,0.5)
tick_position = range(1,5)
ax.set_xticks(tick_position)
ax.set_xticklabels(num_clos,rotation=45)
plt.show()

