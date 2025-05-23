class Collage:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def display_info(self):
        print(self.name,self.age,self.roll_no)
class AIML(Collage):
    def __init__(self,name, age,roll_no,grade):
        super().__init__(name,age,roll_no)
        self.grade = grade
    def welcome(self):
        print('Welcome\n',self.name,self.age,self.roll_no,self.grade)

s = AIML('Kali',18,21,9)
s.display_info()
print(s.grade)
s.welcome()