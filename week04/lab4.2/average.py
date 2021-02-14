#average.py
# this program will continue to read numbers until the user enters 0
# it will print out the entered numbers and their average
# author: Katie Mc Donald

numbers = []

number = int(input('Please enter a number (or press 0 to quit)'))

while number != 0:               #adding the number to the list if no 0
    numbers.append(number)
    number = int(input('Please enter a number (or press 0 to quit)'))

for num in numbers:
    print(num)

average = float(sum(numbers) / len(numbers)) #len() get the lenght 
print('The average is', float(average))