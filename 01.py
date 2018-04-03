'''
定义一个学生类
'''

class Student():
    #定义一个空类
    pass

#定义一个对象
mingyue = Student()


#定义一个学习Python的学生类
class PythonStudent():
    #用None给不确定的变量赋值
    name = 'zf'
    age = 18
    course = ['Python','Java','Php']


    #定义个一个做功课的方法
    def doHomework(self):
        print('我在做功课')
        return None

#查看类的内容
#print(PythonStudent.__dict__)
print(PythonStudent.name)
print(id(PythonStudent.name))
print(PythonStudent.course)
print(id(PythonStudent.course))
print('*' * 20)
#实例一个学生
yueyue = PythonStudent()
print(yueyue.name)
print(id(yueyue.name))
print(yueyue.course)
print(id(yueyue.course))
#yueyue.doHomework()
print('*' * 20)
a='zf'
print(a)
print(id(a))
c=['Python','Java','Php']
print(c)
print(id(c))