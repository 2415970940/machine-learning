import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fandango = pd.read_csv('fandango_score_comparison.csv')
cols = ['FILM','RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
rows =fandango[cols]

num_clos = ['RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
score = fandango[num_clos]
values = score.ix[0,num_clos].values
print(values)
bar_position = np.arange(4)+0.75

fig,ax = plt.subplots()
ax.barh(bar_position,values,0.5)

tick_position = range(1,5)
ax.set_yticks(tick_position)
ax.set_yticklabels(num_clos,rotation=45)

ax.set_ylabel("rating source")
ax.set_xlabel("score")
ax.set_title("flim")

plt.show()