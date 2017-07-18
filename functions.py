# -*- coding: utf-8 -*-
'''
Created on 2017年6月29日

@author: Administrator
'''
#isinstance
import math
def my_abs(x):
    #参数检查
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x;
    else:
        return -x;

# print(my_abs(13))
    
#返回多个值,其实是返回一个tuple
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle);
    ny = y + step * math.sin(angle);
    return nx,ny
