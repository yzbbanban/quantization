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
print('====> ', s.values)
print('====>>', s.index)
print('----->', s[:2])
# 以常量值为数据类型创建 Series对象。
s = pd.Series(5, index=["a", "b", "c", "d", "e"])
print(s)

# 列表组成的字典形式创建
df = pd.DataFrame({'one': [1., 2., 3., 5], 'two': [1., 2., 3., 4.]})
print(df)

# 以嵌套列表形式创建
df = pd.DataFrame([[1., 2., 3., 4.], [2., 3., 1., 3.]], index=["a", "b"], columns=["one", "two", "three", "four"])
print(df)

# 以二维 ndarray 创建
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'hello'), (2, 3., 'world')]
df = pd.DataFrame(data, index=["first", "second"], columns=["C", "A", "B"])
print(df)

# 字典形式创建

data = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
        'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
dfc = pd.DataFrame(data, index=['d', 'b', 'a'], columns=['two', 'one'])
print(dfc)
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df)

# 以字典的字典创建
df = pd.DataFrame({('a', 'b'): {('A', "B"): 1, ("A", "C"): 2},
                   ('a', 'a'): {('A', "C"): 3, ("A", "B"): 4},
                   ('a', 'c'): {('A', "B"): 5, ("A", "B"): 6},
                   ('b', 'a'): {('A', "C"): 7, ("A", "B"): 8},
                   ('b', 'b'): {('A', "D"): 9, ("A", "B"): 10},
                   })
print(df)

print("-----------------------------")

# DateFrame数据访问对象
print(dfc)
print(dfc.index)
print(dfc.columns)
print(dfc.values)




