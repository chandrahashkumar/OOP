class Car:
    def __init__(self,Name,Speed,Color):
        self.Name = Name
        self.Speed = Speed
        self.Color = Color
    def speed_decr(self,speed):
        if speed > 0:
            self.Speed -= speed
    def speed_incre(self,speed):
        self.Speed += speed
    def speed_disp(self):
        print(self.Speed)

Name = input("Enter your car name: ")
Speed = int(input("Enter your car speed: "))
Color = input("Enter your car color: ")
Nano = Car(Name,Speed,Color)
Nano.speed_decr(20)
Nano.speed_disp()





