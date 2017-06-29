# -*- coding: utf-8 -*-
'''
Created on 2017年6月29日

@author: Administrator
'''
classmates = ["Michael","Boy","Tracy"]
for name in classmates:
    print(name)
    
#range(begin,end) 生成一个包含begin，小于end的整数序列
sum_num = 0;
for x in range(1,101):
    sum_num += x;
print(sum_num)
print("---------------while---------------------")
s1 = 0;
n = 99;
while n > 0:
    s1 += n;
    n -= 2;
print(s1)
print("---------------dict---------------------")
#同java map,key必须是不可变对象
d = {"Michael":34,"Boy":88,"Tracy":98}
print(d['Michael'])
#key不存在，报错
#print(d['Thoms'])
#判断key存在不存在
#method 1
hasKey = 'Thoms' in d
print(hasKey)
#method 2，使用dict提供的get方法，可以返回None，也可以返回指定的value
print(d.get('Thoms'))
print(d.get('Thoms',-1))
print("---------------set---------------------")
#无序不重复集合
print(set([1,2,2,3,4,5]))