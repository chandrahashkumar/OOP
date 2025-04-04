import time
class Parent:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")

tx= Parent()
tk = None
time.sleep(5)
print(tx)

