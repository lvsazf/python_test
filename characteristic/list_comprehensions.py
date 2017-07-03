# -*- coding: utf-8 -*-
'''
Created on 2017年7月3日

@author: Administrator
'''
import os
'列表生成式,x * x 写在前面，后面跟循环'
#指定范围的 1*1 2*2 3*3
print([x * x for x in range(10)])
#加判断，只取偶数的平方
print([x * x for x in range(10) if x % 2==0])
#两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])
#遍历当前目录下所有的文件和目录
print([f for f in os.listdir('.')])
#字符串转小写,如果元素不是字符串，则忽略
L = ['Hello', 'World', 18, 'Apple', None]
print([v for v in L if isinstance(v, str)])