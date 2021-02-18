#queue.py
#this program puts 10 random numbers in a queue(list) and outputs the values in the queue
# it will then take the numbers from the queue one at a time, print it and
#the rest of the numbers still in the queue
#Author: Katie Mc Donald

import random

queue = []
ten_random_numbers = 10
range_to = 100

for number in range(0, ten_random_numbers):
    queue.append(random.randint(0,range_to))

print('the queue is:', queue)

while len(queue) != 0:        #when the lenght of the queue is not 0
    #current_number becomes the one removed at the start of the queue
    current_number = queue.pop(0)
    print('Current Number:', current_number, 'The remaining numbers in the queue are:', queue)

print('Queue is now empty')