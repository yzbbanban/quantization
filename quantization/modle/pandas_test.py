import numpy as np
import pandas as pd

s = pd.Series(["这是什么", -1.242312, -1.24323, -1.4343145, -1.24354], index=["a", "b", "c", "d", "e"])
print(s)

# dtype 指定为 int8
s = pd.Series([-1.2343, -1.242312, -1.24323, -1.4343145, -1.24354], index=["a", "b", "c", "d", "e"], dtype='int8')
print(s)

# ndarry 数据类型创建 series 对象
s = pd.Series(np.random.random(5), index=["a", "b", "c", "d", "e"])
print(s)

# 以字典为数据类型创建 Series对象。
s = pd.Series({'a': 0, 'b': 1, 'c': 2}, index=["a", "b", "c", "d", "e"])
print(s)


# 以常量值为数据类型创建 Series对象。
s = pd.Series(5, index=["a", "b", "c", "d", "e"])
print(s)
