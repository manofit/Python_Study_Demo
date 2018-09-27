d = {'a':'A', 'b':'B', 'c':'C'}
if 'a' in d:
    print('a in d')

print(d.get('a')) # A
print(d.get('d')) # None
print(d.get('d', -1)) # -1

# 删除
d.pop('a')


# set集合，需要传入一个list初始化，无序性、唯一性。
s = set([1,2,3])
print(s) # {1, 2, 3}
# 重复的元素会被set过滤掉
s_1 = set([1,2,2,3,4,4])
print(s_1) # {1, 2, 3, 4}
# 添加
s_1.add(5)
# 删除
s_1.remove(4)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2) # {2, 3}
print(s1 | s2) # {1, 2, 3, 4}

s3 = {1,2,3}
print(type(s3))