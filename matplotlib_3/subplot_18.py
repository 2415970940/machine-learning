import pandas as pd
import matplotlib.pyplot as plt
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(8,5))
colors = ['red','blue','black','green','orange']
for i in range(5):
    label = str(1948+i)
    plt.plot(unrate[i*12:(i+1)*12]['MONTH'],unrate[i*12:(i+1)*12]['VALUE'],c=colors[i],label=label)
plt.legend(loc='best')
print(help(plt.legend))
plt.show()