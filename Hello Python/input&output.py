poem = '''\
Programing is fun
when the work is done
if you wanna make your work also fun
    use python!
'''

#以'w'riting方式打开文件
f = open('poem.txt', 'w')
#向文件编写文本
f.write(poem)
#关闭文件
f.close()

#如果没有特别指定，将启用默认的阅读('r'ead)模式
f = open('poem.txt')
while True:
    line = f.readline()
    #0长度指示
    if len(line) == 0:
        break
    #每行的末尾，都已经有了换行符，因为它是从一个文件中进行读取
    print(line,end='')
f.close()


#pickle
import pickle

#我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
#需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

#准备写入文件
f = open(shoplistfile, 'wb')
#存储对象至文件
pickle.dump(shoplist, f)
f.close()

#清除shoplist变量
del shoplist

#重新打开存储文件
f = open(shoplistfile, 'rb')
#从文件中载入对象
storedlist = pickle.load(f)
print(storedlist)

#unicode
import io

f = io.open('abc.txt', 'wt', encoding='utf-8')
f.write(u'imagine non-english here')
f.close()

text = io.open('abc.txt', encoding='utf-8').read()
print(text)

#当我们阅读或者写入某一个文件或者放我们希望与其他计算机交互的时候，我们将我们的unicode
#字符串转换成一个能被发送和接收的格式，这个格式就是utf-8。