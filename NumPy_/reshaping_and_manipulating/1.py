import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])

reshaped_arr = arr.reshape(4,2)
print(reshaped_arr) # create a view that mean change original array