import time


def poll(i):
    if i > 10:
        return 5
    return 0


i = 0
while not (nodes := poll(i)): time.sleep(1); i += 1
