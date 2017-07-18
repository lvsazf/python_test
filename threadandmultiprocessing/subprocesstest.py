# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: lzs
'''
#使用subprocess启动一个子进程
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('exist code : ',r)