import time


def time_it(func):
    def wrappers(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " function took "+ str((end-start)*1000) + " milli second to execute.")
        return result
    return wrappers

@time_it
def calc_sqr(number):
    return number*number

calc_sqr(22)