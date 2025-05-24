# Polymorphism
class Plane:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")
class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")

p = Plane("Boeing", 747)
b = Boat("Ibiza","Touring 20")
c = Car("BMW","BMW2025")
for i in (p,b,c):
   i.move()