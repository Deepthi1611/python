# class variables
class Car:
    totalCars=0
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model
        Car.totalCars += 1

    def getBrand(self):
        return self.__brand

    def fuelType(self):
        return 'petrol or diesel'

myCar = Car("Toyota", "Corolla")
myCar2 = Car("Toyota", "Corolla")
print(Car.totalCars)
myCar3 = Car("Toyota", "Corolla")
print(Car.totalCars)