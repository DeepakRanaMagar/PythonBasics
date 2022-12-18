# Line, Scatter, Area Charts
# Histogram , Bar
# Pie, Box Plot
# Parallel Coordinates

# multiple plot
import matplotlib.pyplot as plt
import numpy as np 
# plot 1
x = np.array([0,5,10,15])
y = np.array([10,20,30,40])
plt.subplot(3,3,1)
plt.plot(x,y)
plt.title("Graph 1")
# plot 2 

x = np.array([1,2,3])
y = np.array([5,6,7])
plt.subplot(2,2,2)
plt.plot(x,y)
plt.title("Graph 2")


# supertitle
plt.suptitle("Multiple Plots")
plt.show()
