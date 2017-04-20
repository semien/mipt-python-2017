import sys
from functools import wraps


def memoize(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        if (args, kwargs) not in decorate.argslist:
            res = func(*args, **kwargs)
            decorate.argslist += [(args, kwargs)]
            decorate.results += [res]
            return res
        else:
            return decorate.results[decorate.argslist.index((args, kwargs))]

    decorate.argslist = []
    decorate.results = []
    return decorate

exec(sys.stdin.read())
