#try...except
try:
    text = input('Enter a number --> ')
except EOFError:
    print('EOF error')
except KeyboardInterrupt:
    print('you called the operation')
else:
    #没有发生异常时候触发
    print('You entered {}'.format(text))


#抛出异常
#通过raise语句来引发一次异常，你能够引发的错误或者异常必须是直接或者间接从属于Exception类的派生类
class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    #其他工作能在此处继续正常运行
except EOFError:
    print('EOF error')
except ShortInputException as ex:
    print('ShortInputException: the input was ' + '{0} long, excepted at least {1}'.format(ex.length, ex.atleast))
else:
    print("it's ok")


#try...finally
import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush() # 可以被立即打印到屏幕
        print('press ctrl+c now')
        #为了确保他能运行一段时间
        time.sleep(2)
except IOError:
    print('could not find file poem.txt')
except KeyboardInterrupt:
    print('you cancelled the reading from the file')
finally:
    if f:
        f.close()
    print('cleaning up: closed the file')


#with
#上面的操作可以：
with open('poem.txt') as f:
    for line in f:
        print(line, end='')