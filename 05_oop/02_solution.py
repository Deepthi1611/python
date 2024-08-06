class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def printName(self):
        # print(self.brand, self.model)
        return f"{self.brand}{self.model}"

myCar = Car("Toyota", "Corolla")
# myCar.printName()
print(myCar.printName())
print(myCar.brand, myCar.model)