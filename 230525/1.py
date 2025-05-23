class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name

    def info(self):
        print(f"Welcome {self.f_name} {self.l_name}")
class Student(Person):
    pass

s1 = Student("Chandrahash","Kumar")
s1.info()