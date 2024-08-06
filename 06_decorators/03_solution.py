import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if(args in cache_value):
            print('inside if')
            print(cache_value)
            return cache_value[args]
        else:
            print('inside else')
            res = func(*args)
            cache_value[args] = res
            return res
    return wrapper

@cache
def longRunningFunction(a, b):
    time.sleep(4)
    return a+b

print(longRunningFunction(1,2))
print(longRunningFunction(1,2))
print(longRunningFunction(1,2))
print(longRunningFunction(1,2))
print(longRunningFunction(4,2))