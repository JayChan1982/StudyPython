'''
定义一个学生类，用来描述学生
'''
class Student():
    # 一个空类，pass代表直接跳过
    #此处pass必须有
    pass

#定义一个对象
jay = Student()

#定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要主意
    # def的缩进级别需要主意，在class后面一个级别，跟内部变量一个级别
    # 系统默认由一个self参数[后续确认是什么？]
    def doHomeWork(self):
        print("i doing the homework")
        #推荐在函数末尾使用return语句，无返回就用return none
        return None



#实例化一个叫jay的对象
jay = PythonStudent()
jay.doHomeWork()
jay.name = "jay"
print(jay.name)

#内置函数列举类的变量和函数
#obj.__dict__
#class_name.__dict__
print(PythonStudent.__dict__)
print(jay.__dict__)





