#传递元祖
def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()
print(errnum)
print(errstr)


#python中交换两个变量的最快方法
a = 5; b = 6
a, b = b, a
print((a, b))


#列表推导
#从一份现有的列表中得到另一个列表
listone = [1,2,3,4]
listtwo = [i * 2 for i in listone if i > 2]
print(listtwo)


#定义一个能够接受任意参数的函数
def function(*args, **keys):
    pass


#assert 断言 语句
#我确定下面的事情是真的，如果不是真的，会抛出AssertionError错误
mylist= ['a']
assert len(mylist) >= 1
mylist.pop()
assert len(mylist) >= 1


#装饰器
from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger('retry')

def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception('attempt %s/%s failed : %s,',
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)

        log.critical('all %s attempt failed : %s',
                     MAX_ATTEMPTS,
                     (args, kwargs))

    return wrapped_f

counter = 0

@retry
def save_to_database(arg):
    print('write to a database or make a network call or etc')
    print('this will be automatically retried if exception is throw')

    global counter
    counter += 1
    #这将在第一次调用的时候抛出异常
    #在第二次运行时候将正常工作
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database('some bad value')