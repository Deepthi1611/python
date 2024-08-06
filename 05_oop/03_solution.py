class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def printName(self):
        # print(self.brand, self.model)
        return f"{self.brand} {self.model}"

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize

myCar = ElectricCar('Tesla', 'model s', '85KWH')
print(myCar.model, myCar.brand, myCar.batterySize)
print(myCar.printName())