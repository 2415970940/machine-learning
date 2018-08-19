import numpy as np
# 有合就有分
a = np.floor(10*np.random.random((2,12)))
print(a)
# 切三分
print(np.hsplit(a,3))
# 在第3列和第4列切一刀
print(np.hsplit(a,(3,4)))

b = np.floor(10*np.random.random((6,2)))
print(b)
print(np.vsplit(b,2))