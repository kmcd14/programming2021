# convert.py
# this program takes in a float amount in dollars and outputs the absolute amount in cents
# author: Katie Mc Donald

import math

deposit = input('please enter the amount you wish to deposit: ')

# turn the amount entered in to cents 
# replaces '.' with a nothing 
dollars_to_cents = deposit.replace('.', '') 

int_cents = int(dollars_to_cents) #changes string to integer
absolute_amount = abs(int_cents)  # we can now get the absolute value 

print(absolute_amount)