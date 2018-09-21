#方法
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hi,',self.name)

p = Person('clf')
p.say_hi()


#类变量：是共享的，可以被属于该类的所有实例对象访问，而且只有一个副本，任何一个对象对类变量的修改都会在其他对象访问的时候体现出来。
#对象变量：不是共享的，只能被单独的实例对象访问，即一个实例对象拥有自己单独的对象变量。
class Robot:
    '''表示有一个带有名字的机器人'''

    #一个类变量，用来计算机器人的数量
    __population = 0 # __开头的变量，外部无法访问

    def __init__(self,name):
        '''初始化数据'''
        self.name = name
        print('(initialize {})'.format(self.name))

        #当有机器人被创建的时候，数量加1
        Robot.__population += 1

    def die(self):
        '''挂了'''
        print('{} is being destroyed!'.format(self.name))

        Robot.__population -= 1
        #等效于 self.__class__.population -= 1

        if Robot.__population == 0:
            print('{} was the last robot'.format(self.name))
        else:
            print('there are still {:d} robots working'.format(Robot.__population))

    def say_hi(self):
        '''来自机器人的问候'''
        print('hi, my name is'.format(self.name))

    @classmethod
    def how_many(cls):
        '''打印当前人口的数量'''
        print('we have {:d} robots'.format(cls.__population))

r1 = Robot('r1')
r1.say_hi()
#等效于 r1.__class__.say_hi()  因为每个对象都能通过self.__class__来引用它的类
Robot.how_many()

r2 = Robot('r2')
r2.say_hi()
Robot.how_many()

r1.die()
r2.die()

Robot.how_many()