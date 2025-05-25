import numpy as np
arr_2d = np.array([[5,6],
                   [4,3]])

new_arr_2d = np.insert(arr_2d,2,[1,2],axis=1)
print(new_arr_2d)