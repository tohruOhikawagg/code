import threading

memory = {}

lock = threading.Lock()

def set_value(key, value):
    global memory
    global lock
    lock.acquire()
    memory[key] = value
    lock.release()

def get_value(key):
    global memory
    global lock
    lock.acquire()
    value = memory.get(key, None)
    lock.release()
    return value

def thread_1():
    set_value("a", 25)
    set_value("b", 18)
    print("Thread 1 sets value of a as 25 and b as 18")

def thread_2():
    value_a = get_value("a")
    value_b = get_value("b")
    print("Thread 2 reads value of a as {} and b as {}".format(value_a, value_b))
    set_value("c", value_a * value_b)

def main_thread():
    thread1 = threading.Thread(target=thread_1)
    thread2 = threading.Thread(target=thread_2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    value_c = get_value("c")
    print("Main thread reads value of c as {}".format(value_c))

if __name__ == "__main__":
    main_thread()
