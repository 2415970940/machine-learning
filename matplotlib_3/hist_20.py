import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fandango = pd.read_csv('fandango_score_comparison.csv')
cols = ['FILM','RottenTomatoes','RottenTomatoes_User','Metacritic','Metacritic_User']
rows =fandango[cols]

r_distribution = rows['RottenTomatoes'].value_counts()
r_distribution = r_distribution.sort_index()

m_distribution = rows['Metacritic'].value_counts()
m_distribution = m_distribution.sort_index()

fig,ax = plt.subplots()
#  将向量rows['RottenTomatoes']中的元素分到n个等间隔的范围内(默认为10个间隔)，并返回每个范围内元素的个数作为一行向量。
# ax.hist(rows['RottenTomatoes'])
ax.hist(rows['Metacritic'],bins=20)
ax.set_ylim(0,20)

plt.show()