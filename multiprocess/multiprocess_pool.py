from multiprocessing import Pool, Process, cpu_count
import os
import time

def long_time_task(i):
    print('subprocess: %s, mission: %d' % (os.getpid(), i))
    time.sleep(2)
    print("result: %d" % (8**20))

if __name__ == "__main__":
    print('CPU core: %d' % cpu_count())
    print('mainprocess: %s' % os.getpid())
    start = time.time()
    #p = Pool(4)
    p = Pool(cpu_count())
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print('wait for all subprocess')
    p.close()
    p.join()
    end = time.time()
    print('Total time: %d sec' % (end-start))
