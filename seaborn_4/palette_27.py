import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set_style("darkgrid")
# multivariate_normal(mean, cov, size=None, check_valid=None, tol=None)
x,y = np.random.multivariate_normal([0,0],[[1,-.5],[-.5,1]],size=300).T
pal = sns.dark_palette("green",as_cmap=True)
sns.kdeplot(x,y,cmap=pal)
plt.show()