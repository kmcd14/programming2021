# random_fruit.py
# this program prints out a random fruit
# author: Katie Mc Donald

import random

fruits = ['Apple', 'Orange', 'Banana', 'Peach', 'Cherry', 'Kiwi']

# fruits are assigned a number. -1 is always the last item in the list
index = random.randint(0, len(fruits) -1)
fruit = fruits[index]


print('A random fruit: {}'.format(fruit))