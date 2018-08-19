import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

# sns.set()
# sinplot()
# plt.show()

"""
5 theme style:
darkgrid
whitegrid
dark
white
ticks

"""
sns.set_style("whitegrid")
data = np.random.normal(size=(20,6))+np.arange(6)/2
sns.boxplot(data=data)
sns.despine()
plt.show()
