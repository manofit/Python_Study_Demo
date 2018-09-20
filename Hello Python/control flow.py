#if
number = 23
guess = int(input('Enter a number:')) #input函数将以字符串的形式返回我们输入的内容

if number == guess:
    print('you guess it')
elif guess < number:
    print('it is higher than you guess')
else:
    print('it is smaller than you guess')

print('Done')


#while
number_1 = 23
running = True

while running:
    guess_1 = int(input('Enter a number:'))

    if guess_1 == number_1:
        print('you guess it')

        running = False
    elif guess_1 < number_1:
        print('it is higher than you guess')
    else:
        print('it is smaller than you guess')
else:
    print('the while loop end in this')

print('Done')


#for
for i in range(5):
    print(i)
else:
    print('the for loop is over')
# range(1,5)   输出[1,2,3,4]
# range(1,5,2)   输出[1,3]
# range()每次只会返回一个数字，如果需要得到完整的数字列表，需要使用list()
# list(range(1,5))   [1,2,3,4]


#break  终止循环，不再执行循环
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('Length for something is',len(s))
print('Done')


#continue  跳出当前循环，执行下一次循环
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('input is of sufficient length')