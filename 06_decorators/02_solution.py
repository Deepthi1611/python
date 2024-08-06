def debug(func):
    def wrapper(*args, **kwargs):
        argsValue = ', '.join(str(arg) for arg in args)
        kwargsValue = ', '.join(f"{key} : {value}" for key,value in kwargs.items())
        print(f"function - {func.__name__}, with args - {argsValue} and with keyword args - {kwargsValue}")
        func(*args, **kwargs)
    return wrapper

@debug
def example(firstName, lastName, greeting = "hello"):
    print(f"{greeting} {firstName} {lastName}")

example('Deepthi', 'Purijala', greeting= "hai")