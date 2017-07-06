# -*- coding: utf-8 -*-
'''
Created on 2017年7月6日

@author: luzs
'''
import os
from multiprocessing import Process, Pool
import time
import random


def myThread(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


# threadpool
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent Process %s' % os.getpid())
#     p = Process(target=myThread, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
        
    p = Pool(4)
      
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
          
