import matplotlib.pyplot as plt 
import numpy as np
values = np.array([10,20,30])
items = ["A","B","C"]
plt.pie(values, labels=items,startangle =90)
plt.legend()
plt.show()
