# -*- coding: utf-8 -*-
'''
Created on 2017年6月30日

@author: Administrator
'''

'a test module' #任何模块代码的第一个字符串都视为模块的文档注释
__author__ = 'lvsazf'#写如作者名

import sys
from PIL import Image
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello,world')
        img=Image.open('C:/Users/Administrator/Desktop/img/toolbar.png')
        print(img.format,img.size,img.mode)
    elif len(args)==2:
        print('Hello,%s',args[1])
    else:
        print('to many argument')
if __name__ == '__main__':
    test()
    