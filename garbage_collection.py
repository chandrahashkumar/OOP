class Person:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


k = Person()
k2 = k
del k
del k2