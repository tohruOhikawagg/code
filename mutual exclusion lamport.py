from threading import Thread
import time

class LamportMutex:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.clock = [0] * num_processes
        self.in_cs = [False] * num_processes
        self.queue = []

    def request_cs(self, pid):
        self.clock[pid] += 1
        self.queue.append((self.clock[pid], pid))
        self.queue.sort()
        print(f"Process {pid} is requesting to enter the critical section.")
        while self.queue[0][1] != pid or self.queue[0][0] != self.clock[pid]:
            time.sleep(0.1)
            if self.in_cs[self.queue[0][1]]:
                print(f"Process {pid} is waiting to enter the critical section.")
        self.in_cs[pid] = True

    def release_cs(self, pid):
        self.in_cs[pid] = False
        self.queue.pop(0)

def process(mutex, pid):
    while True:
        mutex.request_cs(pid)
        print(f"Process {pid} is in the critical section.")
        time.sleep(1)
        print(f"Process {pid} is exiting the critical section.")
        mutex.release_cs(pid)
        time.sleep(1)

if __name__ == "__main__":
    num_processes = 3
    mutex = LamportMutex(num_processes)
    threads = []

    for i in range(num_processes):
        t = Thread(target=process, args=(mutex, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
