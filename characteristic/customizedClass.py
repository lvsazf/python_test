'''
Created on 2017年7月5日

@author: lzs
'''

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name;
    def __str__(self):
        return 'Student object (name: %s)  ' % self.__name
print(Student('Michael'))
#其它不想去看了。。。