import numpy as np
# np.nan_to_num(array,nan=value) -> default value is 0

arr = np.array([10,20,np.nan,7,9,np.nan])
cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

arr1 = np.array([12,3,6,np.nan,4])
cleaned_arr1 = np.nan_to_num(arr1,nan = 500)
print(cleaned_arr1)