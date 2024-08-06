class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model
 
myCar = Car("Toyota", "Corolla")
print(isinstance(myCar, Car))