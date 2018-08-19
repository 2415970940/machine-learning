import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fandango = pd.read_csv('fandango_score_comparison.csv')

fig,ax = plt.subplots()
ax.scatter(fandango['RottenTomatoes'],fandango['RottenTomatoes_User'])
ax.set_ylabel('RottenTomatoes_User')
ax.set_xlabel('RottenTomatoes')
plt.show()