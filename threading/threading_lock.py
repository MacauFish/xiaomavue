import threading

class Account:
    def __init__(self):
        self.balance = 0
    
    def add(self, lock):
        lock.acquire()
        for i in range(0, 100000):
            self.balance += 1
        lock.release()

    def delete(self, lock):
        lock.acquire()
        for i in range(0, 10000):
            self.balance -= 1
        lock.release()
    
if __name__ == "__main__":
    account = Account()
    lock = threading.Lock()

    threading_add = threading.Thread(target=account.add, args=(lock,), name='add')
    threading_delete = threading.Thread(target=account.delete, args=(lock,), name='delete')

    threading_add.start()
    threading_delete.start()

    threading_add.join()
    threading_delete.join()

    print('The final balance is: %d' % account.balance)