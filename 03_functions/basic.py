# generator function in python
# generator function that yields even numbers upto a specified limit 
# generator function returns value through yield but it remembers memory of the function and upto which it has been executed
# if generator function is called from two different places, python remembers memory of both generator functions
# and upto where execution is completed in both the cases
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)


# recursive function to calculate the factorial of a number
def factorial(number):
    if(number == 0):
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))