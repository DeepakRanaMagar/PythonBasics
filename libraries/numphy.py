import numpy as np

a = np.array([[1,2,3], [4,5,6]])
b = a[a % 2 == 0]

print(b)