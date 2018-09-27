# 位置参数
def power(x):
    pass

# 默认参数
def power_2(x, n=2):
    pass

# 位置参数必须在前，默认参数在后；
# 默认参数必须指向不可变对象；
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L

# 可变参数
def calc(*numbers):
    pass

calc(1,2,3)

numbers =[1,2,3]
calc(*numbers)

# 关键字参数
def person(name, age, **kw):
    pass

extra = {'city':'shanghai', 'job':'iOS', 'where':'kongjiang'}
person('gaojun', 25, **extra)
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数，只能接收指定的参数
def person_1(name, age, *, city, job):
    pass

person_1('gaojun', 25, city='shanghai', job='iOS')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person_2(name, age, *args, city, job):
    pass

# 命名关键字参数可以有缺省值：
def person_3(name, age, *, city='shanghai', job):
    pass

person_3('gaojun', 24, job='iOS')

