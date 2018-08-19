import numpy as np
import pandas as pd
from pandas import DataFrame,Series

ser = Series(np.arange(3.))
# print(ser)
data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
print(data)

data.sort_values('w',ascending=False,inplace=True)
print(data)
