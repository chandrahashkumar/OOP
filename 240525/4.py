# Pass by Value(immutable type) [int,float,string,tuple]
def sum(a):
    a+=5
    return a
num = 10
print(sum(num))
print(num)