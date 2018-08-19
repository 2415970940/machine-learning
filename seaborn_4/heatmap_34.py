import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set()
np.random.seed(0)

# data = np.random.rand(3,3)
# # heatmap = sns.heatmap(data)
# # colorbar 范围
# heatmap = sns.heatmap(data,vmax=0.5,vmin=0)

# data = np.random.randn(3,3)
# # randn 值有正负
# heatmap = sns.heatmap(data,center=0)

flights = sns.load_dataset("flights")
print(flights.head(2))

flights=flights.pivot('month','year','passengers')
# print(flights.head())
# annot显示数据，fmt数据的格式,linewidths格子间距
# ax = sns.heatmap(flights,annot=True,fmt="d",linewidths=.5)
# cmap调色板.cbar=False隐藏渐进版
ax = sns.heatmap(flights,cmap="YlGnBu",cbar=False)
plt.show()