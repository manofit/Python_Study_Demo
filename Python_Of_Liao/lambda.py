print(list(map(lambda x: x * x, [1,2,3,4,5]))) # [1, 4, 9, 16, 25]

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f = lambda x: x * x
print(f(5)) # 25

# 匿名函数作为返回值
def build(x, y):
    return lambda x, y: x + y