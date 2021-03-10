# plotting.py
# This program plots the function y = xsquared
# Author: Katie Mc Donald

import numpy as np
import matplotlib.pyplot as plt 

xpoint = np.array(range(1,101))
ypoint = xpoint * xpoint #multiply each point by itself

plt.plot(xpoint, ypoint)
plt.show()

