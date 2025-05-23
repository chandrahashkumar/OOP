class University:
    university_name = "Sandip University"
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello {self.name}")

class Branch(University):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch = branch
    def info(self):
        print(f"Name: {self.name}\nBranch: {self.branch}")

class SOCSE(Branch,University):
    pass

s = SOCSE("Chandrahash",'B.Tech AI&ML')
print(s.university_name)
s.greet()
s.info()