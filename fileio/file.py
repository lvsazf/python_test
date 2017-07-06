# -*- coding: utf-8 -*-
'''
Created on 2017年7月5日

@author: lzs
'''
#解决错误UnicodeDecodeError：'gbk' codec can't decode byte 0xba in position 146: illegal multibyte sequence
#open文件指定encoding或者model改为b,以binary方式读取
#文件使用完之后，必须关闭，避免占用系统资源
try:
    f = open('test','r', encoding='utf-8')
    s = f.read()
    print(s)
except FileNotFoundError as e:
    print('except:',e) 
finally:
    if f:
        f.close()


#with使用，自动调用close(),效果同上，代码更简洁
with open('test','w', encoding='utf-8') as  f:
    f.write('test')
    
