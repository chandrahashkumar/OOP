class Student:

    # Constructor
    def __init__(self,name):
        self.name = name
        self.age = 19
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called")


s1 = Student("Altman")
print(s1.name)
s2 = s1
del s2
s1 = None


