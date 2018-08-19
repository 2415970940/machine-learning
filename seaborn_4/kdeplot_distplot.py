import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"distributions")))
"""
ord()函数它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值.
　　如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常.
　　利用np.random.seed()函数设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数.
"""
# x = np.random.normal(size=100)
# sns.distplot(x,bins=20,kde=False)

# 散点图
mean,cov = [0,1],[(1,.5),(.5,1)]
# data = np.random.multivariate_normal(mean,cov,200)
# df = pd.DataFrame(data,columns=["x","y"])
# sns.jointplot(x='x',y='y',data=df)

# x,y = np.random.multivariate_normal(mean,cov,1000).T
# with sns.axes_style("white"):
#    sns.jointplot(x=x,y=y,color="k",kind="hex")

iris = sns.load_dataset("iris")
sns.pairplot(iris)


plt.show()