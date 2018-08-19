import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set(style="white",color_codes=True)
np.random.seed(sum(map(ord,"facetgrid")))

tips=sns.load_dataset("tips")
titanic=sns.load_dataset("titanic")
iris=sns.load_dataset("iris")

# g = sns.FacetGrid(tips,col="time")
# g.map(plt.hist,"tip")

# g = sns.FacetGrid(tips,col="time",hue="smoker")
# # alpha透明度
# g.map(plt.scatter,"total_bill","tip",alpha=.7)
# # 小窗口
# g.add_legend()

# # margin_titles   smoker纵向显示
# g = sns.FacetGrid(tips,col="time",row="smoker",margin_titles=True)
# # fit_reg 显示回归线，x_jitter 抖动
# g.map(sns.regplot,"size","total_bill",color=".4",fit_reg=True,x_jitter=.2)

# ordered_days = tips.day.value_counts().index
# print(ordered_days)
# from pandas import Categorical
# ordered_days = Categorical(['Thur', 'Fri','Sat', 'Sun'])
# g = sns.FacetGrid(tips,row="day",row_order=ordered_days)
# g.map(sns.boxplot,"total_bill")

# _36
#
# pal = dict(Lunch="seagreen",Dinner="gray")
# g = sns.FacetGrid(tips,hue="time",palette=pal,size=5)
# # s点的大小，edgecolor点边的颜色，
# g.map(plt.scatter,"total_bill","tip",s=50,alpha=.7,linewidth=.5,edgecolor="white")
# g.add_legend()

# g = sns.FacetGrid(tips,hue="sex",palette="Set1",size=5,hue_kws={"marker":["^","v"]})
# g.map(plt.scatter,"total_bill","tip",s=50,alpha=.7,linewidth=.5,edgecolor="white")
# g.add_legend()

# with sns.axes_style("white"):
#     g=sns.FacetGrid(tips,row="sex",col="smoker",margin_titles=True)
# g.map(plt.scatter,"total_bill","tip",color="#334488",edgecolor="white",lw=.5)
# g.set_axis_labels("Total Bill($)","Tip")
# g.set(xticks=[10,30,50],yticks=[2,6,10])
# # 子图与子图之间的间隔
# g.fig.subplots_adjust(wspace=.4,hspace=.5)

# g = sns.PairGrid(iris,hue="species")
# # g.map(plt.scatter)
# # 对角线上画图
# g.map_diag(plt.hist)
# g.map_offdiag(plt.scatter)
# g.add_legend()

# g = sns.PairGrid(iris,hue="species",vars=["sepal_length","sepal_width"])
# g.map(plt.scatter)
# g.add_legend()

g = sns.PairGrid(tips,hue="size",palette="GnBu_d")
g.map(plt.scatter,s=50,edgecolor="white")
g.add_legend()

plt.show()