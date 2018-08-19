import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)


# sns.set_style("whitegrid")
# data = np.random.normal(size=(20,6))+np.arange(6)/2
# sns.violinplot(data)
# # 偏离
# sns.despine(offset=10)

# # two styles
# with sns.axes_style("whitegrid"):
#     plt.subplot(211)
#     sinplot()
# plt.subplot(212)
# sinplot()

# sns.set_context("paper")
# sns.set_context("talk")
sns.set_context("poster")
sinplot()
plt.show()