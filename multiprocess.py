import time
import os
from typing import get_args
from multiprocessing import Process

def long_time_task():
    print('当前线程：%s' % (os.getpid()))
    time.sleep(2)
    print('结果：%d' % (8**20))

def long_time_task2(i):
    print("子进程：%d. 任务：%d" % (os.getpid(), i))
    time.sleep(2)
    print("结果：%d" % (8**20))

if __name__ == "__main__":
    print("当前母进程：%s" % os.getpid())
    start = time.time()
    for i in range(2):
        long_time_task()
    end = time.time()
    print("用时 %d 秒" % (end-start))

    print("="*20)
    
    print("当前母进程：%s" % os.getpid())
    start = time.time()
    p1 = Process(target=long_time_task2, args=(1,))
    p2 = Process(target=long_time_task2, args=(2,))
    print("等待子进程完成")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("用时 %d 秒" % (end-start))