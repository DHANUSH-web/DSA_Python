'''
    File Name   : main.py
    File Type   : Python Script
    Feature     : Asynchronous Processing and Thread Processing
    Developer   : Dhanush H V
'''

import threading
import string
import random
import time

data = {}
thread1_count = 0
thread2_count = 0


def pro1() -> None:
    global thread1_count
    for _ in range(5):
        # time.sleep(1)
        name = random.choice(string.ascii_letters)
        data[name] = random.randint(0, 100)
        print(data[name], " is added by Thread1")
        thread1_count += 1


def pro2() -> None:
    global thread2_count
    for _ in range(5):
        # time.sleep(1)
        name = random.choice(string.ascii_letters)
        data[name] = random.randint(0, 100)
        print(data[name], " is added by Thread2")
        thread2_count += 1


try:
    calls = [pro1, pro2]
    threads = []

    for thread in calls:
        t = threading.Thread(target=thread)
        t.daemon = True
        threads.append(t)

    for thread in threads:
        thread.start()
        thread.join()

    print(f"Thread1 Count: {thread1_count}\nThread2 Count: {thread2_count}")
except RuntimeWarning:
    print("Something went wrong")
finally:
    print("Data:", data)
