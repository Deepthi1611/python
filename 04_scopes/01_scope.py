# scope starts with indentation in python

username = 'test1'
def test():
    # username = 'test2'
    print(username)

print(username)
test()

x=99

# def func(y):
#     z = x+y
#     return z

# print(func(1))

# def func2():
#     global x
#     x=88 # this refers to local x, to make this global x we use global keyword
#     # but it is not recommended to change global values

# func2()
# print(x)

def func3():
    x=88
    def func4():
        print(x)
    # func4()
    return func4

# print(func3())
# func3()() 
# In the above line we have executed only func4 but it has printed value of x even though x is not declared inside it
# this phenomenon is called closure, In memory along with the function definition variable references also get stored
# closures are also known as factory functions


def func5(num):
    def func6(x):
        return x**num
    return func6

# res = func5(2)
# print(res)
# # prints square of 3
# print(res(3))
# res2 = func5(3)
# print(res2)
# # prints cube of 3
# print(res2(3))


def func7():
    x=10
    def func8():
        print(x, 'inside func 8')
        def func9():
            print(x, 'inside func 9')
        return func9
    return func8

res = func7()
print(res)
res2 = res()
print(res2)
res3 = res2()
# output is None
# closure are applicable only upto one level, not more than that
print(res3)