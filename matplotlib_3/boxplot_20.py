import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fandango = pd.read_csv('fandango_score_comparison.csv')
cols = ['FILM','RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
rows =fandango[cols]

fig,ax = plt.subplots()
# ax.boxplot(rows['Metacritic'])
# ax.set_xticklabels('Metacritic')
num_clos = ['RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
score = fandango[num_clos].values
ax.boxplot(score)
ax.set_xticklabels(cols,rotation=90)
ax.tick_params(bottom="off",left="off")

plt.show()