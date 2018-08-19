import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set(style="white",color_codes=True)
np.random.seed(sum(map(ord,"categorical")))

tips=sns.load_dataset("tips")
titanic=sns.load_dataset("titanic")
iris=sns.load_dataset("iris")
# sns.stripplot(x="day",y="total_bill",data=tips)
# sns.swarmplot(x="day",y="total_bill",data=tips)
# sns.swarmplot(x="day",y="total_bill",data=tips,hue="sex")

# sns.boxplot(x="day",y="total_bill",data=tips,hue="time")
# sns.violinplot(x="day",y="total_bill",data=tips,hue="time")
# sns.violinplot(x="day",y="total_bill",data=tips,hue="sex",split=True)

# sns.barplot(x="sex",y="survived",hue="class",data=titanic)
# sns.pointplot(x="class",y="survived",hue="sex",data=titanic,palette={"male":"g","female":"m"},
#               markers=["^","o"],linestyles=["--","-"])

# sns.boxplot(data=iris,orient="h")

# 多层面板分类图
# sns.factorplot(data=tips,x="day",y="total_bill",hue="smoker",kind="bar")
# sns.catplot(data=tips,x="day",y="total_bill",hue="smoker",kind="bar")
# sns.catplot(data=tips,x="day",y="total_bill",col="sex",hue="smoker",kind="swarm")
sns.catplot(data=tips,x="time",y="total_bill",col="day",hue="smoker",kind="swarm",size=4,aspect=.5)

plt.show()