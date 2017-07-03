# -*- coding: utf-8 -*-
'''
Created on 2017年6月30日

@author: Administrator
'''
'切片，对指定索引范围的操作'
#语法：
#a[start:end] 从start到end-1
#a[start:] 从start到末尾
#a[:end] 从开头到end结束
#a[:] 复制整个列表
#a[start:end:step] 按照step步长到end-1

#创建一个0-99的序列
L = list(range(100))
#从索引1开始到索引3结束，但不包含3
print(L[1:3])
#如果第一个索引是0，可以省略
print(L[:3])
#取倒数第一个元素,倒数第一个元素的索引是-1
print(L[-1])
#取索引0-19之间的偶数（步长为2)
print(L[0:20:2])
#如果取值不在范围内，返回空
print(L[101:])
nL = L[0:30:3]
#返回一个list
print(isinstance(nL, list))