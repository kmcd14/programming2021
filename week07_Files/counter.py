# counter.py
# This program will count how many times it was run
# Author: Katie Mc Donald

# a function which reads from a file that exists
filename = 'count.txt'
def read_counter():
    with open(filename) as f:
        count = int(f.read())
        return count


#test 
counter = read_counter()
print(counter)

