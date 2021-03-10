# ages.py
# This program makes a list of ages that has the same number of random values as funwithnum.py.
#  and makes a scatter plot for the data 
# Author: Katie Mc Donald

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
entries = 100

#keeps random numbers the same values
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, entries)
ages = np.random.randint(low=21, high=65, size=entries)

# scatter plot
plt.scatter(ages, salaries)
plt.show()

# plot
xpoint = np.array(range(1,101))
ypoint = xpoint * xpoint 

plt.plot(xpoint, ypoint, color='green', label= 'x squared')
plt.title('random plot')
plt.xlabel('Salaries')
plt.ylabel('age')
plt.legend()
#plt.show()
#saving the plot
plt.savefig('randomplot.png')
