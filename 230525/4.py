class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # string representation, it is always return string, no call needed
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def info(self):
        return f"Hello {self.name}, and your age is {self.age}"

p = Person('Jone',19)
print(p)
p.info()


p = Person("Kali", 19)
print(p.info())