#单例模式:一个类只能实例出一个对象，共用一套数据，什么时候用单例对象，例如配置，一处修改了，其他的都要一致，一起修改，整个项目中只用一个对象
#为什么要用单例：单例，只要实例化，就只是一个对象，有5种创建单例的方式
#目前先说两种
#只要支持面向对象的都有单例模式，属于一种软件设计的风格

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

alex = Person("alex",33)
egon = Person("egon",32)


#单例模式 ---方法一（基于业务方式，利用__new__的方法做出来的）
class Singleton(object):
    _instance = None   # _instance为内存空间变量
    def __new__(cls,*args,**kwargs):
        if not cls._instance:  #如果_instance为空，要执行以下代码 #第一次实例化的时候一定是空，所以运行以下代码
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)  #执行父类方法，调用__new__方法
        return cls._instance   #最终返回这个实例对象

class MyClass(Singleton):
    a = 1


mc1 = MyClass()   #第一次实例化，没有值，执行父类方法，返回一个值

mc2 = MyClass()   #第二次实例化，有值，执行父类方法，直接返回那个值，即上一次实例化出的那个对象

mc3 = MyClass()   #第一次实例化后，以后再实例化，就取第一次实例化的内容

#三次实例化出的是一个实例对象

# print(id(mc1))
# print(id(mc2))
# print(id(mc3))
# print(mc1)

#单例模式 ---方法二（基于模块的单例模式）：模块方式， python独有的方式
#python的一个特点：加载模块只加载一遍,（导入多次同一个模块，模块加载只加载一遍）
import admin学习教程笔记.modelsdemo.func
import admin学习教程笔记.modelsdemo.func

from admin学习教程笔记.modelsdemo.mysingleton import my_singleton,My_Singleton   #利用模块实现单例对象-1
my_singleton.foo()  #利用模块实现单例对象-2

# from admin学习教程笔记.modelsdemo.mysingleton import my_singleton as my_singleton_new
# my_singleton_new.foo()
#
print(id(my_singleton))
# print(id(my_singleton_new))

from admin学习教程笔记.modelsdemo import func

func.bar()

#思考3

ms1 = My_Singleton()
ms2 = My_Singleton()
ms3 = my_singleton

print(id(ms1))
print(id(ms2))
print(id(ms3))
