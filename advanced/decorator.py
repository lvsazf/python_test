# -*- coding: utf-8 -*-
'''
Created on 2017年7月4日

@author: luzs
'''

# 通过函数对象的__name__属性可以拿到函数的名字


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 把@log放到定义处，就相当于执行了insert = log(insert)
@log
def insert():
    print("insert into db")


def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log1('execute')
def insert1():
    print("insert into db")

insert1()