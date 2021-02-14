# guess2.py
# this program asks the user to guess a number.
# It will tell the user if their guess is too high or low
# the program will keep prompting the user to guess the number until correct
# author: Katie Mc Donald

import random

number_to_guess = random.randint(1,101)

guess = int(input('Please guess a number between 1 and 100: '))

while guess != number_to_guess:
    if guess < number_to_guess:
        print('too low')
    else:
         print('too high')
    guess = int(input('Please guess again: '))

print('Congratulations! you guessed correct! The number was', number_to_guess)