import sys
from functools import wraps


def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(0, min(len(args),len(types))):
                if types[i] != type(args[i]):
                    raise TypeError(" ")
            return func(*args, **kwargs)
        return wrapper
    return decorator

exec(sys.stdin.read())
