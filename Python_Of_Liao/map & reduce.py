def f(x):
    return x * x

r = map(f, [1,2,3,4,5])
print(list(r)) # [1, 4, 9, 16, 25]
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

print(list(map(str, [1,2,3,4,5])))
# ['1', '2', '3', '4', '5']

from functools import reduce

# reduce(f, [1,2,3,4]) = f(f(f(1,2),3),4)
def add(x, y):
    return x + y

print(reduce(add, [1,3,5,7,9])) # 25

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1,2,3,4,5])) # 12345

# str2int函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('12345')) # 12345

