array_1 = ['a', 'b', 'c', 'd']
# 追加
array_1.append('e')
# 指定位置添加
array_1.insert(1, 'g')
# 末尾删除
array_1.pop()
# 指定位置删除
array_1.pop(1)
# 修改元素
array_1[1] = 'h'

# 数组中的元素也可以是不同类型的
array_2 = ['a', 2, True]

# 声明一个空数组
array_3 = []
len(array_3) # 0


t = ('a', 'b', ['c', 'd'])
t[2][0] = 'e'
t[2][0] = 'f'
print(t) # ('a', 'b', ['f', 'd'])
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！