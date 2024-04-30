import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def deadlock_thread1():
    if lock1.acquire(timeout=2): 
        print("Thread 1 acquired lock 1")
        time.sleep(1) 
        print("Thread 1 waiting to acquire lock 2")
        if lock2.acquire(timeout=2): 
            print("Thread 1 acquired lock 2")
            lock2.release()
        else:
            print("Thread 1 failed to acquire lock 2, terminating...")
        lock1.release()
    else:
        print("Thread 1 failed to acquire lock 1, terminating...")

def deadlock_thread2():
    if lock2.acquire(timeout=2): 
        print("Thread 2 acquired lock 2")
        time.sleep(1)
        print("Thread 2 waiting to acquire lock 1")
        if lock1.acquire(timeout=2):
            print("Thread 2 acquired lock 1")
            lock1.release()
        else:
            print("Thread 2 failed to acquire lock 1, terminating...")
        lock2.release()
    else:
        print("Thread 2 failed to acquire lock 2, terminating...")

thread1 = threading.Thread(target=deadlock_thread1)
thread2 = threading.Thread(target=deadlock_thread2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program finished execution")
