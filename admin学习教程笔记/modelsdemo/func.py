print("OK")

from admin学习教程笔记.modelsdemo.mysingleton import my_singleton
def bar():
    my_singleton.foo()
    print(id(my_singleton))
