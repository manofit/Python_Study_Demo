class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized schoolmember : {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}", Age:"{}"'.format(self.name,self.age), end=' ')

class Teacher(SchoolMember):
    '''老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(initialized teacher : {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(initialized student : {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mr.Ding', 30, 10000)
s = Student('gaojun', 15, 90)

#打印一空白行
print()

members = [t, s]
for member in members:
    member.tell()


