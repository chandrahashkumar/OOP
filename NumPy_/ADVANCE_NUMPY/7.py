"""
vstack() row wise
hstack() column wise
"""
import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

print(np.vstack((arr1,arr2)))  #vertically stack
print(np.hstack((arr1,arr2)))  #horizontally stack

