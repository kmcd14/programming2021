# counties.py
# this program demostrates making a pie plot of unique values in an array
# Author: Katie Mc Donald

import numpy as np
import matplotlib.pyplot as plt

choice_of_counties = ['Louth', 'Galway', 'Antrim', 'Limerick', 'Wicklow']

#p – The probability attach with every samples in first parameter i.e. counties 
counties = np.random.choice(choice_of_counties, p=[0.1, 0.3, 0.2, 0.12, 0.28 ], size =(100)) 
# creates a tuple of the unique  values and the amount of times they appear
unique, counts = np.unique(counties, return_counts=True)

#piechart
plt.pie(counts, labels=unique)
plt.show()

#barchart
plt.bar(unique, counts)
plt.show()
