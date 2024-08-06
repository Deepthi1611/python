import time

def timer(func):
    def wrapper(*args):
        startTime = time.time()
        res = func(*args)
        endTime = time.time()
        print(f"{func.__name__} ran in {endTime-startTime}")
        return res
    return wrapper

@timer
def example(n):
    time.sleep(n)
    print('inside example function')

example(2)
# whenever example function is called, it first goes through the timer decorator
# wrapper is returned to the timer decorator and it is called
# inside the wrapper function func() is executed and then result is returned