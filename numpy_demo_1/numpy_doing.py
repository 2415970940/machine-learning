import numpy as np
a = np.arange(3)
print(a)
print(np.exp(a))
print(np.sqrt(a))

b = np.floor(10*np.random.random((3,4)))
print(b)
# matrix -> vetor
print(np.ravel(b))
b.shape = (2,6)
print(b)
print(b.T)

# reshape(3,-1) 默认-1，程序计算

