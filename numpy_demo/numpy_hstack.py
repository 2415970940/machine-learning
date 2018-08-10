import numpy as np
# 矩阵拼接
a = np.floor(10*np.random.random((3,4)))
b = np.floor(10*np.random.random((3,4)))
print(a)
print(b)
print(np.hstack((a,b)))
print(np.vstack((a,b)))
# vstack增加样本

