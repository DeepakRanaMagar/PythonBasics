import numpy as np

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

arr[0] = 100

print(arr)
print(x.base)
print(y.base)