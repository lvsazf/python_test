# -*- coding: utf-8 -*-
'''
Created on 2017年7月4日

@author: luzs
'''
class Student(object):
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise TypeError('score must be a int');
        if value < 0 or value > 100:
            raise ValueError('score must be betweeen 0 ~ 100')
        self.__score = value
# s = Student()
# s.score = 99

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width * self.__height

screen = Screen()
screen.width = 2;
screen.height = 111;
print(screen.resolution)
    
