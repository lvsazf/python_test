# -*- coding: utf-8 -*-
'''
Created on 2017年7月6日

@author: luzs
'''
from multiprocessing import Process, Pool
import os
import time
import random

#子进程
def myProcess(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


# threadpool
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 
if __name__ == '__main__':
#     print('Parent Process %s' % os.getpid())
#     p = Process(target=myProcess, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
#####################################################################
#对pool对象调用join方法会等待所有子进程执行完毕，调用join之前必须先close，close之后就不能再添加新的process了    
    pool = Pool(4)      
    for x in range(5):
        pool.apply_async(long_time_task,args=(x,))
    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()
    print('All subprocesses done.')