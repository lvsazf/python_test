# -*- coding: utf-8 -*-
'''
Created on 2017年7月3日

@author: Administrator
'''
from collections import Iterable
from _collections_abc import Iterator
'判断是否是Iterable'
#可以直接作用于for循环的对象统称为可迭代对象，Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('123', Iterable))
print(isinstance(123, Iterable))
print(isinstance((x for x in range(10)), Iterable))
print('---------------------')
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('123', Iterator))
print(isinstance(123, Iterator))
print(isinstance((x for x in range(10)), Iterator))
#可以把list dict str通过iter()转为Iterator
print('---------------------')
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('123'), Iterator))
print(isinstance(123, Iterator))
print(isinstance((x for x in range(10)), Iterator))
#for本质上就是不断调用next()来实现的