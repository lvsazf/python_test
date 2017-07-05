# -*- coding: utf-8 -*-
'''
Created on 2017年7月5日

@author: lzs
'''
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


#value是自动赋值给成员的int常量
for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


#更精确的控制枚举类型,@unique检查保证没有重复值
@unique
class Weekday(Enum):
    Sum = 0;
    Mon = 1;
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Sum
print(day1 == Weekday.Sum)