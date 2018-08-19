import pandas as pd
data = [[1,2,3],[4,5,6]]
index = [0,1]
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
"""
    a b c
0   1 2 3
1   4 5 6
"""



# 1. loc——通过行标签索引行数据
df.loc[1]
'''''
a    4
b    5
c    6
'''

# 1.2 loc[‘d’]表示索引的是第’d’行（index 是字符）
import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)

"""
    a b c
d   1 2 3
e   4 5 6
"""

df.loc['d']
'''''
a    1
b    2
c    3
'''

# 1.3 如果想索引列数据，像这样做会报错
# print (df.loc['a'])
'''''
KeyError: 'the label [a] is not in the [index]'
'''

# 1.4 loc可以获取多行数据
print (df.loc['d':])
'''''
   a  b  c
d  1  2  3
e  4  5  6
'''

# 1.5 loc扩展——索引某行某列

print(df.loc['d',['b','c']])
'''''
b    2
c    3
'''

# 1.6 loc扩展——索引某列

print (df.loc[:,['c']])
'''''
   c
d  3
e  6
'''

"""
当然获取某列数据最直接的方式是df.[列标签]，但是当列标签未知时可以通过这种方式获取列数据。

需要注意的是，dataframe的索引[1:3]是包含1,2,3的，与平时的不同。

2. iloc——通过行号获取行数据

2.1 想要获取哪一行就输入该行数字
"""
df.iloc[1]
'''''
a    4
b    5
c    6
'''

# 2.2 通过行标签索引会报错

# print (df.iloc['a'])
'''''
TypeError: cannot do label indexing on <class 'pandas.core.index.Index'> with these indexers [a] of <type 'str'>
'''

# 2.3 同样通过行号可以索引多行

df.iloc[0:]
'''''
   a  b  c
d  1  2  3
e  4  5  6
'''

# 2.4 iloc索引列数据

df.iloc[:,[1]]
'''''
   b
d  2
e  5
'''

# 3. ix——结合前两种的混合索引

# 3.1 通过行号索引

df.ix[1]
'''''
a    4
b    5
c    6
'''

# 3.2 通过行标签索引

df.ix['e']
'''''
a    4
b    5
c    6
'''