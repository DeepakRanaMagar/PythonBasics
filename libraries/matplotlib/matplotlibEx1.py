# Line, Scatter, Area Charts
# Histogram , Bar
# Pie, Box Plot
# Parallel Coordinates

import matplotlib.pyplot as plt
import numpy as np 

xaxis = np.array([0,5])
yaxis = np.array([0,50])

plt.title("TIME AND DISTANCE TO REACH DESTINATION", loc= 'left')
plt.grid()
# plt.grid(axis="x")

plt.plot(xaxis, yaxis, marker = 'o', ms = 20, mec = "black",mfc="green", ls="--", c = "purple", lw = 10) 
plt.plot(yaxis, marker="*")

plt.xlabel("distance")
plt.ylabel("time")

plt.show()

