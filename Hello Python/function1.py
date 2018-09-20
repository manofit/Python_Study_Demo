def say_hello():
    print('hello')

say_hello()
say_hello()


#使用参数
def print_max(a,b):
    if a < b:
        print(b,'is max')
    elif a > b:
        print(a,'is max')
    else:
        print(a,'is equal',b)

print_max(3,4)

x = 5
y = 7
print_max(x,y)


#局部变量
x = 50

def func(x):
    print('x is',x)   # 50
    x = 2
    print('local x is',x)   # 2

func(x)
print('x is still',x)   # 50


#global
#global x,y,z
x = 50

def func_1():
    global x

    print('x is',x)    # 50
    x = 2
    print('change global x to',x)    # 2

func_1()
print('x now is',x)    # 2


#默认参数值
def say(message, times=1):
    print(message * times)

say('hello')    # hello
say('hello', 5)    # hellohellohellohellohello


#关键字参数
#不再需要考虑参数的顺序，可以只对希望赋予的参数以赋值
def func_2(a, b=5, c=10):
    print('a is',a,'and b is',b,'and c is',c)

func_2(3,7)    # a is 3 and b is 7 and c is 10
func_2(25,c=23)    # a is 25 and b is 5 and c is 23
func_2(c=40,a=34)    # a is 34 and b is 5 and c is 40


#可变参数
#当我们声明一个诸如*params的星号参数时，从此处开始直到结束的所有位置参数都将被收集并汇集成一个名为params的元祖
#当我们声明一个诸如**params的星号参数时，从此处开始直到结束的所有关键字参数都将被收集并汇集成一个名为params的字典
def func_3(a=5,*numbers,**phonebook):
    print('a',a)

    for single_item in numbers:
        print('single_item',single_item)

    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(func_3(10,1,2,3,jack=1123,john=2231,inge=1560))
# a 10
# single_item 1
# single_item 2
# single_item 3
# inge 1560
# john 2231
# jack 1123
# None


#return
#python中的函数不需要指定return的类型，可以返回任何类型
#return语句没有搭配任何一个值则代表返回None
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'equal'
    else:
        return y
print(maximum(2,3))
#每一个函数都在其末尾隐含了一句return None，除非你自己写了自己的return语句
def some_function():
    pass    # pass用于指示一个没有内容的语句块
print(some_function())    # None


#DocStrings 文档字符串
def print_max_1(x,y):
    '''打印两个数值的最大值。

    这两个数都应该是整数'''
    x = int(x)
    y = int(y)

    if  x > y:
        print(x,'is max')
    else:
        print(y,'is max')

print_max_1(3,5)    # 5 is max
print(print_max_1.__doc__)
# 打印两个数值的最大值
# 这两个数都应该是整数
