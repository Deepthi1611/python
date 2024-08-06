# polymorphism
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model

    def getBrand(self):
        return self.__brand

    def fuelType(self):
        return 'petrol or diesel'

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def fuelType(self):
        return 'electricity'

myCar = ElectricCar('Tesla', 'model s', '85KWH')
print(myCar.fuelType())
myCar2 = Car("Toyota", "Corolla")
print(myCar2.fuelType())