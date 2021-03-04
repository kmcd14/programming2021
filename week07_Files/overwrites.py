# overwrites.py
# This program takes in a number + overwrites a file (count.txt) with that number 
# Author: Katie Mc Donald

filename = 'count.txt'
def overwrite_count(number):
    with open(filename, 'wt') as f:
        f.write(str(number))

#test
overwrite_count(5)