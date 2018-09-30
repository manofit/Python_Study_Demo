# python中为了节约内存，仅在使用的时候推算出来，这种方式创建列表的方式叫做：生成器。

# 创建生成器
# 方法一：把一个列表生成式的[]改为()
g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x101279a98>
# 打印出生成器的元素，使用next()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

# 生成器也是可迭代对象
for n in g:
    print(n)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81


# 方法二：将函数的print(b)改为yield b
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 如果一个函数中包含yield，那么就不再是一个函数，而是一个生成器。
f = fib(6)
print(f) # <generator object fib at 0x10a339b10>

# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

for n in fib(6):
    print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g :',x)
    except StopIteration as e:
        print('return value :',e.value)
        break
# g : 1
# g : 1
# g : 2
# g : 3
# g : 5
# g : 8
# return value : done