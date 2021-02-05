# random_generator.py
# this program will output a random number between 1 and 10
# author: Katie Mc Donald

import random

print('Please enter the range you would to generate a random number from')
x = int(input('please enter the first number: '))
y = int(input('please enter your second number: '))

number = random.randint(x, y)
print('here is a random number between {} and {}: \n{}'.format(x, y, number))