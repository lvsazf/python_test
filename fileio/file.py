# -*- coding: utf-8 -*-
'''
Created on 2017年7月5日

@author: lzs
'''
#解决错误UnicodeDecodeError：'gbk' codec can't decode byte 0xba in position 146: illegal multibyte sequence
#open文件指定encoding或者model改为b,以binary方式读取
try:
    f = open('D:/svn.hw/trunk/basecode1.txt','r', encoding='utf-8')
    s = f.read()
    print(s)
except FileNotFoundError as e:
    print('except:',e) 
finally:
    if f:
        f.close()