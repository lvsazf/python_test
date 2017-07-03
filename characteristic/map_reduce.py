# -*- coding: utf-8 -*-
'''
Created on 2017年7月3日

@author: Administrator
'''
# map 第一个参数是函数对象本身，第二个是个Iterable，map将传入的函数依次作用到序列的每个函数上，并把结果做为新的Iterator返回
from _functools import reduce


def f(x):
    return x * x


L = map(f, range(10))
print(list(L))
# 将0-9转为字符串
print(list(map(str, range(10))))


#############################################
# reduce把函数作用在另一个序列上，这个函数必须接收两个参数，把结果和序列的下一个元素做累计计算
# 1-9求和
def add(x, y):
    return x + y


print(reduce(add, range(10)))


# 将1、3、5、7、9 转为13579
def fn(x, y):
    if not isinstance(x, int):
        raise TypeError('x must be a int')
    if not isinstance(y, int):
        raise TypeError('y must be a int')
    return x * 10 + y


print(reduce(fn, range(1, 10, 2)))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '13579')))


# 用lambda
def str2int(s):
    return reduce(lambda x, y: x * 10 + x, map(char2num, s))
print(str2int('13579'))


#将传进来的名字首字母大写，其余小写
names = ['adam', 'LISA', 'barT']
def normalize(name):
    return map(str.capitalize,name)
print(list(normalize(names)))

#接收一个list并求积
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print(list(range(1,5)))
print(prod(range(1,5)))