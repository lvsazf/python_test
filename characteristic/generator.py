# -*- coding: utf-8 -*-
'''
Created on 2017年7月3日

@author: Administrator
'''
'生成器'
#method 1,把列表生成式的[]改为() 
g = (x for x in range(10))
print(g)
#next()获取generator的下一个返回值
print(next(g))
#一般用for来遍历generator
# for n in g:
#     print(n)
#斐波拉契数列 1,1,2,3,5,8,13...
def fib(m):
    n,a,b = 0,0,1;
    while n<m:
        print(b);
        a,b = b,a+b;
        n+=1;
    return 'None'
fib(10)
#把fib变成generator
def fib1(m):
    n,a,b = 0,0,1;
    while n<m:
        yield b;
        a,b = b,a+b;
        n+=1;
    return 'None'
f = fib1(10)
print(f)
#generator 和一般函数的区别：
#一般函数顺序执行，到return或最后一行返回
#generator遇到yield返回，再次调用从上次返回的yield执行
def odd():
    print('step1')
    yield 1;
    print('step2')
    yield 2;
    print('step3')
    yield 3;
o = odd()
print(next(o))
print(next(o))
print(next(o))
#如果没有更多元素，则抛出StopIteration异常
#print(next(o))
#获取generator的return返回值,捕获StopIteration异常，返回值包含在StopIteration的value中
while True:
    try:
        v = next(o)
        print(v)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break