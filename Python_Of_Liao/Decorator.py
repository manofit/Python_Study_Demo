def now():
    print('2018-9-29')

f = now
f() # 2018-9-29

print(f.__name__) # now
print(now.__name__) # now

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个接收函数并返回函数的高阶函数

def log(func):
    def wrap(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrap

@log
def now_1():
    print('2018-9-29')

now_1() # 相当于now_1 = log(now_1)
# call now_1():
# 2018-9-29


# 如果装饰器需要传入参数：
def log(text):
    def deractor(func):
        def wrap(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrap
    return deractor

@log('call')
def now_2():
    print('2018-9-29')

now_2() # 相当于 now_2 = log('call')(now_2)
# call now_2():
# 2018-9-29


