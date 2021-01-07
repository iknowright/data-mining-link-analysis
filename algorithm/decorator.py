import time


def execution_timer(func):
    """
    timer for execution
    """

    def wrapper(*args):
        start = time.time()
        func_ret = func(*args)
        elapsed = time.time() - start
        print(f'{func.__name__}:time {elapsed} elapsed second(s)')
        return func_ret
    return wrapper
