# guess1.py
# this program asks the user to guess a number
# the program will keep prompting the user to guess the number until correct
# author: Katie Mc Donald

import random

number_to_guess = random.randint(1,10)

guess = int(input('Please guess a number between 1 and 10: '))

while guess != number_to_guess:
    print('Wrong')
    guess = int(input('Please guess again: '))

print('Congratulations! you guessed correct! The number was', number_to_guess)