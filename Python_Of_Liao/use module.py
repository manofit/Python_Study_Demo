#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'gao jun'

import sys

def test():
    args = sys.argv # 用list存储的来自命令行的所有参数
    if len(args) == 1:
        print('hello, world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many args')

if __name__ == '__main__':
    test()


# 作用域
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用。
# private函数或变量不应该被别人引用，那它们有什么用呢？
def _private_1(name):
    return 'hello, %s' % name

def greeting(name):
    return _private_1(name)

# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了。
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法。