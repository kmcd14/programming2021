# topthree.py
#this program generates 10 random numbers and prints out the top three
#Author: Katie Mc Donald

import random

how_many_num = 10
top_three = 3
range_start = 0
range_end = 100

numbers = []

#getting the 10 random numbers and storing them in a list
for num in range(0,10):
    numbers.append(random.randint(range_start, range_end))
print(how_many_num, 'random numbers:',numbers)

top_num = numbers.copy() # means modification in new list won’t be reflected to original list 
top_num.sort(reverse=True) #reverses the order 
print('The top', top_three, 'are:\t',top_num[0:top_three])
