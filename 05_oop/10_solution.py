# multiple inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

class Battery:
    def batteryInfo(self):
        print('thus is battery')
        
 
class Engine:
    def engineInfo(self):
        print('this is engine')

class ElectricCar(Battery, Engine, Car):
    pass

myCar = ElectricCar("Toyota", "Corolla")
myCar.engineInfo()
myCar.batteryInfo()