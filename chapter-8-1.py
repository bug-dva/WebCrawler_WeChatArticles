import thread
import time


def func(name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print name, time.ctime(time.time()), count

thread.start_new_thread(func, ('Thread-1', 3))
thread.start_new_thread(func, ('Thread-2', 2))

while True:
    pass



