"""
np.insert(array, index, value, axis=None)
array - original array
axis = 0, row-wise
axis = 1 , column-wise
"""
import numpy as np

arr = np.array([10,20,30,40,50,60])
new_arr = np.insert(arr,3,5,axis=0) # optional axis
print(new_arr)
print(arr)