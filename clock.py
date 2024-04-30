from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime

def local_time(counter):
    return f'(LAMPORT TIME ={counter}, LOCAL TIME = {datetime.now()})'

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

def event(pid, counter):
    counter += 1
    print('\nEvent happened in {} !'.format(pid) + local_time(counter)) 
    return counter

def send_message(pipe, pid, counter): 
    counter += 1
    pipe.send(('Empty shell', counter))
    print('\nMessage sent from ' + str(pid) + local_time(counter)) 
    return counter

def recv_message(pipe, pid, counter): 
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter) 
    print('\nMessage received at ' + str(pid) + local_time(counter)) 
    return counter

def process_one(pipe12): 
    pid = getpid()
    counter = 0
    counter = event(pid, counter)
    counter = send_message(pipe12, pid, counter) 
    counter = event(pid, counter)
    counter = recv_message(pipe12, pid, counter) 
    counter = event(pid, counter)

def process_two(pipe21, pipe23): 
    pid = getpid()
    counter = 0
    counter = recv_message(pipe21, pid, counter) 
    counter = send_message(pipe21, pid, counter) 
    counter = send_message(pipe23, pid, counter) 
    counter = recv_message(pipe23, pid, counter)

def process_three(pipe32, pipe34): 
    pid = getpid()
    counter = 0
    counter = recv_message(pipe32, pid, counter) 
    counter = send_message(pipe32, pid, counter) 
    counter = send_message(pipe34, pid, counter) 
    counter = recv_message(pipe34, pid, counter)

def process_four(pipe43, pipe45): 
    pid = getpid()
    counter = 0
    counter = recv_message(pipe43, pid, counter) 
    counter = send_message(pipe43, pid, counter) 
    counter = send_message(pipe45, pid, counter) 
    counter = recv_message(pipe45, pid, counter)

def process_five(pipe54): 
    pid = getpid()
    counter = 0
    counter = recv_message(pipe54, pid, counter) 
    counter = send_message(pipe54, pid, counter)

if __name__ == '__main__': 
    oneTwo, twoOne = Pipe() 
    twoThree, threeTwo = Pipe()
    threeFour, fourThree = Pipe()
    fourFive, fiveFour = Pipe()

    process1 = Process(target=process_one, args=(oneTwo,))
    process2 = Process(target=process_two, args=(twoOne, twoThree)) 
    process3 = Process(target=process_three, args=(threeTwo,threeFour))
    process4 = Process(target=process_four, args=(fourThree, fourFive))
    process5 = Process(target=process_five, args=(fiveFour, ))

    process1.start()
    process2.start() 
    process3.start() 
    process4.start()
    process5.start()
    
    process1.join() 
    process2.join() 
    process3.join()
    process4.join()
    process5.join()
