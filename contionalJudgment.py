# -*- coding: utf-8 -*-
'''
Created on 2017年6月29日

@author: Administrator
'''
#    根据python的缩进规则，条件为true，就把缩进的两行全执行了
age = 20;
if age > 28:
    print('your age is',age )
    print('adult')
elif age > 18:
    print('teenager')
else:
    print('kid')
    
'''
用户输入
int() 将数字字符串转为数字
input：用户输入
'''
print('请输入任意数字...........')
number = int(input('birth:'))
if number < 2000:
    print('00前')
else:
    print('00后')

    