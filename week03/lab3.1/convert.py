# convert.py
# this program takes in a float amount in dollars and outputs the absolute amount in cents
# author: Katie Mc Donald

import math

deposit = input('please enter the amount you wish to deposit: ')
dollars_to_cents = deposit.find('.')

cents = int(dollars_to_cents)
absoute_cents = abs(cents)

print(dollars_to_cents)