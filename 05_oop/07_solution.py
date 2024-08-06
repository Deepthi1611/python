# static method - method that belongs to a class instead og=f reference of a class
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model

    def getBrand(self):
        return self.__brand

    @staticmethod
    def func():
        print('static method')

myCar = Car("Toyota", "Corolla")
# myCar.func()
Car.func()