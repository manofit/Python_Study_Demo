# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行。
# 通过collections模块的Iterable类型判断是否是可迭代对象：
from collections import Iterable

if isinstance('abc', Iterable):
    print('abc is iterable')

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 0 A
# 1 B
# 2 C

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key,value)


for x, y in [(1,1), (2,3), (3,9)]:
    print(x,y)