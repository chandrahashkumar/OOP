import numpy as np

while True:
    a = list(map(int,input("Enter V1 components: ").split()))
    b = list(map(int, input("Enter V2 components: ").split()))
    if len(a) and len(b) == 2 or 3 and len(a) == len(b):
        break
    print("Number of component in vector must be 2 or 3 and equal each other. Please try again.")
v1 = np.array(a)
v2 = np.array(b)
cross_product = np.cross(v1, v2)
print(f"Cross product: {cross_product}")