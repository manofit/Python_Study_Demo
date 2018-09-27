# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 所以如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii')) # b'ABC'
print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'
print('中文'.encode('ascii'))
# Traceback (most recent call last):
#   File "/Users/gaojun/Desktop/Python_Study_Demo/Python_Of_Liao/string & code.py", line 10, in <module>
#     print('中文'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 纯英文的str可以用ASCII编码为bytes，内容是一样的。
# 含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii')) # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 中文

# 如果bytes中包含无法解码的字节，decode()方法会报错：
print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
# Traceback (most recent call last):
#   ...
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 长度
print(len('ABC')) # 3
# len()函数计算的是str的字符数，如果换成bytes，len()计算的就是字节数。
print(len('中文'.encode('utf-8'))) # 6
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

#!/usr/bin/env python3
# -*- coding: utf-8 -*- # 为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('hello {0}, your score is {1:.2f}'.format('gaojun', 99.999))

# python中，当str和bytes互相转换时，需要指定编码，最常用的编码是UTF-8。