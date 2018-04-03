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
    name = None
    age = 18
    course = 'Python'


    #定义个一个做功课的方法
    def doHomework(self):
        print('我在做功课')
        return None


#实例一个学生
yueyue = PythonStudent()
yueyue.doHomework()
