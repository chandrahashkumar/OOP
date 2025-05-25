import numpy as np
arr = np.array([10,20,30,np.inf,45,6,-np.inf])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=100,neginf=-100)
print(cleaned_arr)