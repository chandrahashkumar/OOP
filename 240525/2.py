# polymorphism with inheritance

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move")
class Car(Vehicle):
    def move(self):
        print("Drive")

class Boat(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("Fly")

p = Plane("Boeing","885")
b= Boat("Ibiza","Touring 20")
c = Car("BMW", "BMW2024")
for x in(p,b,c):
    print(x.brand)
    print(x.model)
    x.move()