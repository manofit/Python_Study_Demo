#列表，可变的
shoplist = ['apple','mango','carrot','banana']

print('i have',len(shoplist),'items to buy')

print('these items are:',end=' ') # 以空格结尾，而不是以\n结尾，下面的打印语句不会另起一行。
for item in shoplist:
    print(item, end=' ')

print('\ni alse have to buy rice')
shoplist.append('rice')
print('my shoplist is now',shoplist)

print('i will sort my shoplist')
shoplist.sort() # 列表按照首字母排序
print('sorting shoplist is',shoplist)

print('the first item i will buy is',shoplist[0])
olditem  = shoplist[0]
del shoplist[0]
print('i buy the',olditem)
print('my shoplist is now',shoplist)


#元祖，不可变的
zoo = ('python','elephant','penguin')
print('number of animals in the zoo is',len(zoo))

new_zoo = 'monkey','camel',zoo
print('number of cages in the new zoo is',len(new_zoo)) # 3
print('all animals in the new zoo is',new_zoo) # all animals in the new zoo is ('monkey','camel',('python','elephant','penguin'))
print('animals brought from old zoo are',new_zoo[2])
print('last animal brought from old zoo is',new_zoo[2][2])
print('number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2])) # 5

empty_tuple = ()
only_one_tuple = (2,)


#字典，字典的键必须是不可变的对象
ab = {'a':'A','b':'B','c':'C','d':'D'}

print("a's value is",ab['a'])

del ab['d']

print('\nthere are {} contants in the ab dic'.format(len(ab)))

for key,value in ab.items():
    print('Contact {} is {}'.format(key,value))

ab['e'] = 'E'

if 'e' in ab:
    print("\ne's value is",ab['e'])


#序列
#索引
#[-index]，从后往前第index个，index>=1
#切片操作：
#[index1:index2:step]，从index1开始到index2结束，包括index1，不包括index2，step为步长
#[index1:]，从index开始到尾结束
#[:index2]，从头开始到index2结束
#[:]，从头开始到尾结束，相当于复制整个序列
list = ['a','b','c','d']
name = 'asdfghj' # python中字符串也是一种序列，是不可变的


#集合，无序性，唯一性
# >>> a = set(['a','b','c','d'])
# >>> 'a' in a
# True
# >>> 'e' in a
# False
# >>> a_copy = a.copy()
# >>> a_copy.add('e')
# >>> a_copy.issuperset(a)  # a_copy是否是a的父集合
# True
# >>> a.remove('d')
# >>> a_copy & a  # 交集
# {'b', 'c', 'a'}
# >>>