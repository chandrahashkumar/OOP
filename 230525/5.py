class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age


c = Animal('Cat',1)
c.age = 2   # modify object properties , Here set Cat age 1 to 2
print(c.age)
del c.age  # Delete the age property from the c object
del c # Delete the object


