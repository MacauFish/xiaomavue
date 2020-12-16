import threading
import time

def long_time_task(i):
    print('subthreading: %s, mission: %d' % (threading.current_thread().name, i))
    time.sleep(2)
    print("result: %d" % (8**20))

if __name__ == "__main__":
    print("main threading：%s" % threading.current_thread().name)
    start = time.time()
    t1 = threading.Thread(target=long_time_task, args=(1,))
    t2 = threading.Thread(target=long_time_task, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("用时 %d 秒" % (end-start))
