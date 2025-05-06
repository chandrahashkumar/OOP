class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    def __del__(self):
        print("Object deleted")


r = Person(input("Enter your name: "),int(input("Enter your age: ")))
r.info()
del r
