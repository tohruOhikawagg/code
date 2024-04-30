import threading
import time
import os

project_group_member_roll_no_arr = ["BEA128", "BEA139", "BEA160", "BEA171"]
project_group_member_name_arr = ["Amogh", "Dhruv", "Shoaib", "Mudit"]

def project_group_member_roll_no():
    for roll_no in project_group_member_roll_no_arr:
        time.sleep(1)
        print(roll_no)
        print(f"Task {roll_no} assigned to thread: {format(threading.current_thread().name)}")
        print(f"ID of process running task {roll_no}: {format(os.getpid())}\n")

def project_group_member_name():
    for name in project_group_member_name_arr:
        time.sleep(1)
        print(name)
        print(f"Task {name} assigned to thread: {format(threading.current_thread().name)}")
        print(f"ID of process running task {name}: {format(os.getpid())}\n")

thread1 = threading.Thread(target=project_group_member_roll_no)
thread2 = threading.Thread(target=project_group_member_name)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished.")
