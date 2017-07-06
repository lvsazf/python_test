# -*- coding: utf-8 -*-
'''
Created on 2017年7月6日

@author: luzs
'''
from io import StringIO
from io import BytesIO
f = StringIO();
f.write('testtest')
print(f.getvalue())

f = BytesIO();
f.write("中文".encode(encoding='utf_8', errors='strict'))
print(f.getvalue())