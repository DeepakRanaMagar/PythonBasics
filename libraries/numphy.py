import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6,7,8])
# c = a + b 


# ---------------------------
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a + b
# print(c)


# ---------------------------
# a = np.array([[3,2,1], [6,5,4]])
# b = np.sort(a, axis=1)
# print(b)

# a = np.array([[3,2,1], [6,5,4]])
# for i in a:
#     print(i)

a = np.array([[3,2,1], [6,5,4]])
b = a.reshape((3,2))
print(b)