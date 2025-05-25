import numpy as np
prices = np.array([100,200,300,400])
discount = 20
final_prices = prices -(prices*discount/100)
print(final_prices)