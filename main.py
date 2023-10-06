'''
    File Name   : main.py
    File Type   : Python Script
    Feature     : Asynchronous Processing and Thread Processing
    Developer   : Dhanush H V
'''

import threading
import string
import random

# storing random data in multi-threading
data = {}


def process(thread_name: str) -> None:
    for _ in range(5):
        name = random.choice(string.ascii_letters)
        data[name] = random.randint(0, 100)
        print(data[name], "is added by", thread_name)

try:
    threads = []

    for i in range(5):
        t = threading.Thread(target=process(f"Thread{i}"))
        t.daemon = True
        threads.append(t)

    for thread in threads:
        thread.start()
        thread.join()
except RuntimeWarning:
    print("Something went wrong")
finally:
    print("Data:", data)
