import numpy as np
import pandas as pd
from pandas import DataFrame,Series

ser = Series(np.arange(3.))
# print(ser)
data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
print(data)

#选择表格中的'w'列，使用类字典属性,返回的是Series类型
print(data['w'])

#选择表格中的'w'列，使用点属性,返回的是Series类型
print(data.w)

#选择表格中的'w'列，返回的是DataFrame类型
print(data[['w']])
#选择表格中的'w'、'z'列
print(data[['w','z']])
#返回第1行到第2行的所有行，前闭后开，包括前不包括后
print(data[0:2] )
# data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
#        #如果采用data[1]则报错
#
#返回第2行的第三种方法，返回的是DataFrame，跟data[1:2]同
print(data.ix[1:2])
#利用index值进行切片，返回的是**前闭后闭**的DataFrame,
        #即末端是包含的
print(data['a':'b'])
#
# #——————新版本pandas已舍弃该方法，用iloc代替———————
# data.irow(0)   #取data的第一行
# print(data.irow(0))
# data.icol(0)   #取data的第一列
#
# ser.iget_value(0)  #选取ser序列中的第一个
# ser.iget_value(-1) #选取ser序列中的最后一个，这种轴索引包含索引器的series不能采用ser[-1]去获取最后一个，这会引起歧义。
# #————————————————————————————-----------------
#
# data.head()  #返回data的前几行数据，默认为前五行，需要前十行则data.head(10)
print(data.head())
# data.tail()  #返回data的后几行数据，默认为后五行，需要后十行则data.tail(10)

#选取DataFrame最后一行，返回的是Series
# data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame
print(data.iloc[-1])
#返回‘a’行'w'、'x'列，这种用于选取行索引列索引已知
print(data.loc['a',['w','x']])
#选取第二行第二列，用于已知行、列位置的选取。
print(data.iat[1,1])

print(data.shape)
print(data.columns)
print(data.loc['a'])