# make model as read only
# property decorator
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.__model = model

    def getBrand(self):
        return self.__brand

    @property
    def getModel(self):
        return self.__model


myCar = Car("Toyota", "Corolla")
# print(myCar.model)
print(myCar.getModel)