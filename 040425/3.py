class Parent:
    def __init__(self):
        print("Hello Child")
        self.k = 20

# class Child(Parent):
#     def __init__(self):     # AttributeError: 'Child' object has no attribute 'k'
#         print("Hello Parent")
class Child(Parent):
    def __init__(self):
        print("Hello Parent")
        super().__init__()



t = Child()
print(t.k)
