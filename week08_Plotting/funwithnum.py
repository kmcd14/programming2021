# funwithnum.py
# This program makes a list ('Salaries') 
#Author: Katie Mc Donald

import numpy as np 
import matplotlib.pyplot as plt 

min_salary = 20000
max_salary = 80000
random_numbers = 10

# seed ensures the random numbers are the same each time
np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, random_numbers)
print(salaries)
#adding arrays
add_salaries = salaries + 5000
print(add_salaries)
#multiplying arrays
multi_salaries = salaries * 1.05 #5%
print(multi_salaries)

new_salaries = multi_salaries.astype(int)
print(new_salaries)

plt.hist(salaries)
plt.show()