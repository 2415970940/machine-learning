import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats,integrate

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"regression")))

tips=sns.load_dataset("tips")
print(tips.head())

# regplot()和Implot()都可以绘制回归关系，推荐regplot()
# sns.regplot(x='total_bill',y='tip',data=tips)
sns.regplot(x='tip',y='size',data=tips,x_jitter=0.5)
plt.show()