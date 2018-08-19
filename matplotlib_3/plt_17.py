import pandas as pd
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
# print(unrate.head(12))

import matplotlib.pyplot as plt
data = unrate.head(12)
plt.plot(data['DATE'],data['VALUE'])
# x轴标注单位的角度
# plt.xticks(rotation = 45)
# x，y名称，title
plt.ylabel("Unemployment Rate")
plt.xlabel("Month")
plt.title("Monthly Unemployment Trends 1948")
plt.show()
