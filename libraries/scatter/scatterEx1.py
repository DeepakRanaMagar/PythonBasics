import matplotlib.pyplot as plt 
import numpy as np 
# scatter plot 1 
xaxis = np.array([1,5,2,4])
yaxis = np.array([5,10,15,20])
plt.scatter(xaxis, yaxis, marker="*", c = "green")
#scatter plot 2 
x = np.array([9,2,7,2])
y = np.array([20,15,10,5])
color = np.array([0,10,20,30])
plt.scatter(x,y, marker="o",c = color, cmap="viridis", alpha=0.5,s=200)
plt.colorbar()

plt.show()
