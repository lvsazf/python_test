'''
Created on 2017年7月2日

@author: Administrator
'''
import types

class Animal(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def run(self):
        print('animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running')    
class Cat(Animal):
    pass    

dog = Dog();


def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(dog)

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running')
run_twice(Tortoise())
print('-----------------------------------------------------')
#type 用来判断对象类型
print(type(12) == int)
print(type(dog) == Dog)
#types判断一个对象是否是函数
def fn():
    pass
print(type(fn) == types.FunctionType)
print((lambda x : x) == types.LambdaType)
print(type((x for x in range(5)))==types.GeneratorType)
#isinstance 判断class类型
print(isinstance(Tortoise(), Animal) and isinstance(Tortoise(), Tortoise))
#dir() 获取一个对象的所有属性和方法，返回一个包含字符串的list
print(dir('ABC'))
print(hasattr(dog, 'name'))