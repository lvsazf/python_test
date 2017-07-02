# -*- coding: utf-8 -*-
'''
Created on 2017年7月2日

@author: Administrator
'''
#在类中的函数，第一个参数是self，表示创建的实例本身，调用的时候不用传该参数
#实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问，外部不能访问
#__name会被Python解释器自动改为_Student__name
class Student(object):
    def __init__(self,name,age):
        self.__name = name;
        self.age = age;
    def getName(self):
        return self.__name
    def toString(self):
        print('%s:%s' % (self.__name,self.age))