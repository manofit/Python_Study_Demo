def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print(f) # <function lazy_sum.<locals>.sum at 0x100454ea0>
print(f()) # 15

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print(f1 == f2) # False