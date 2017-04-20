import sys
from functools import wraps
import time


def profiler(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        if decorate.x == 0:
            decorate.calls = 0
        decorate.x += 1
        decorate.calls += 1
        tim = time.time()
        res = func(*args, **kwargs)
        decorate.last_time_taken = time.time()-tim
        decorate.x -= 1
        return res

    decorate.calls = 0
    decorate.x = 0
    decorate.last_time_taken = 0
    return decorate

exec(sys.stdin.read())
