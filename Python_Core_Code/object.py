#!/usr/bin/env python

print(type(42)) # <class 'int'>
print(type('abc')) # <class 'str'>

a = 3
b = a
if a is b: # 等价于id(a) == id(b)
    print('a is b')
elif a is not b:
    print('a is not b')


if 3 < 4 < 7:
    print('True')

if 3 < 4 < 5 != 6 < 7:
    print('True')

if isinstance(a, int):
    print('a is int type')

if isinstance(a, (int, float, complex)):
    print('a is one of these type')

