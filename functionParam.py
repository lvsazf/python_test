# -*- coding: utf-8 -*-
'''
Created on 2017年6月30日

@author: Administrator
'''
#参数默认值

def power(x,n=2):
    s = 1;
    while n>0:
        n = n-1;
        s *= x;
    return s
print(power(3,3))
#可变参数,对于参数个数不稳定，可用可变参数
def calc(*numbers):
    s = 0;
    for n in numbers:
        s += n * n
    return s

print(calc(1,2,3))
#list/tuple调用可变参数，可变参数在函数调用的时候，自动组装为tuple
nums = [1,2,3,4]
print(calc(*nums))
#关键字参数,在函数调用的时候，将获得一个dict
def person(name,age,**kw):
    print(name,age,'other:',kw)
person("Michael", 19,city="BeiJing")
#命名关键字参数,命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person1(name,age,*,city,job):
    print(name,age,city,job)
person1("Michael", 19,city="BeiJing",job="programmer")
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*：
def person2(name,age,*v,city,job):
    print(name,age,v,city,job)
person2("Michael", 19,2,3,city="BeiJing",job="programmer")
#命名关键字参数可以有缺省值
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person3("Michael", 19,job="programmer")