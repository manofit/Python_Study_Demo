# filter()接受的函数参数必须返回bool类型，列表中满足函数参数为True的将被保存下来，重新组成一个iterable并返回。
def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7]))) # [1, 3, 5, 7]

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', 'B', ' ', None, '']))) # ['A', 'B']