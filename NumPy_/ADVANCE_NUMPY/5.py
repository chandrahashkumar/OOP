import numpy as np
"""
np.delete(array,index,axis=None)
flattern array / 1D
"""
arr = np.array([10,20,30,40])
new_arr = np.delete(arr,1,axis=None)
print(arr)
print(new_arr)