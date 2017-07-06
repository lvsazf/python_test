'''
Created on 2017年7月2日

@author: Administrator
'''
from builtins import int
from types import MethodType

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name;

student = Student('Michael');
student.age = 18
print(student.age)
def setAge(self,age):
    if not isinstance(age, int):
        raise TypeError('age must be a int')
    self.__age = age
student.set_age = MethodType(setAge,student)
student.set_age(22);
print(student.__age)
#限制实例属性名__slots__
#__slots__定义的属性只对当前类属性有效，对继承的子类不起作用
class Animal(object):
    __slots__=('name','age')#用tuple定义允许绑定的属性
animal = Animal();
animal.name = 'Dog'
animal.age=4
#animal.color='white' #由于color没放到__slots__中，所以不能绑定color，否则会得到AttributeError错误