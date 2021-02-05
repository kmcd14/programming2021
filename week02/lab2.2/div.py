# div.py
# this program reads two numbers and outputs an integer answer and remainder
# author: Katie Mc Donald

num_1 = int(input('Please enter your first number. It must be an integer: '))
num_2 = int(input('Please enter a second number. This must also be an integer: '))

answer = int(num_1/num_2)               
remainder = int(num_1 % num_2)

print('{} divided by {} is {} with a remainder of {}'.format(num_1, num_2, answer, remainder))