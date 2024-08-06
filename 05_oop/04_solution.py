# encapsulation
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model

    def getBrand(self):
        return self.__brand
    
    def printName(self):
        # print(self.brand, self.model)
        return f"{self.brand} {self.model}"

myCar = Car('Tesla', 'model s')
# print(myCar.__brand)
print(myCar.getBrand())