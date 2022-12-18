import matplotlib.pyplot as plt
import numpy as np 

plt.title("Bar-Diagram Example")
x = np.array(["X","Y", "Z"])
y = np.array([20,10,30])
plt.bar(x,y, color = "blue", width=0.2)
# plt.barh(x,y, color = "red")
plt.show()
