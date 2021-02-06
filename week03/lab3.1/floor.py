# floor.py
# this program takes in a float and outputs an integer rounded down
# author: Katie Mc Donald

import math

number_to_floor = float(input('enter a float number: '))
floored_number = math.floor(number_to_floor)

print('{} floored is {}'.format(number_to_floor, floored_number))
