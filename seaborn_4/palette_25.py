import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize":(6,6)})

# color_palette()传入matplotlib所支持的颜色
# set_palette()设置所有图的颜色

# current_palette = sns.color_palette()
# sns.palplot(current_palette)

# hls颜色空间
# current_palette = sns.color_palette("hls",8)
# sns.palplot(current_palette)

# current_palette = sns.color_palette("hls",8)
# data = np.random.normal(size=(20,6))+np.arange(6)/2
# sns.boxplot(data=data,palette=current_palette)
# plt.show()

# hls_palette()控制颜色的亮度和饱和度
# lightness     亮度
# saturation    饱和度
# sns.palplot(sns.hls_palette(8,l=.3,s=.5))

# Paired对比
# sns.palplot(sns.color_palette("Paired",8))

# 连续型画板,有浅到深
# sns.palplot(sns.color_palette("Blues"))
# sns.palplot(sns.color_palette("Reds"))
# 由深到浅
# sns.palplot(sns.color_palette("Reds_r"))

# sns.palplot(sns.light_palette("red"))
sns.palplot(sns.dark_palette("red",reverse=True))
plt.show()