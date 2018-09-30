import collections

# iterable 可迭代对象，可作用于for循环的对象，包括list，tuple，dict，set，str。
# iterator 迭代器，可用作于next()函数的对象，比如生成器。

# 可以通过iter()函数将可迭代对象转换为迭代器
if isinstance(iter([]), collections.Iterator):
    print('ok')

if isinstance(iter({}), collections.Iterator):
    print('ok')

if isinstance(iter('str'), collections.Iterator):
    print('ok')

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1,2,3,4,5]:
    pass

# 等价于
it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break