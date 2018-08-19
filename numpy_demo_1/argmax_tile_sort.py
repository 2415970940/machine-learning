import numpy as np

data = np.sin(np.arange(20)).reshape(5,4)
print(data)
index = data.argmax(axis=0)
print(index)
data_max_column = data[index,range(data.shape[1])]
print(data_max_column)

a = np.arange(0,40,10)
print(a)
a_new = np.tile(a,(3,5))
print(a_new)

b = np.array([[3,1,6],[2,8,3]])
print(b)
c = np.sort(b,axis=0)
print(c)
d = np.sort(b,axis=1)
print(d)