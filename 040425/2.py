import time
import sys
class pk:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("destructor called")


t=pk()
p= t
x=p
print(sys.getrefcount(t)) #by default self is passed.
p=None
print(sys.getrefcount(t))
print("Garbage collector is deleting obj")
time.sleep(5)
print("The end")



















