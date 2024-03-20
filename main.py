import multiprocessing as mp
import time


def print_numbers(counter):
    for i in range(5):
        print(counter, i)
        time.sleep(1)


p1 = mp.Process(target=print_numbers, args=("counter #1",))
p2 = mp.Process(target=print_numbers, args=("counter #2",))

p1.start()
p2.start()

p1.join()
p2.join()
