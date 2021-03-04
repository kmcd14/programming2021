# both_functions.py
# This program uses the read + overwite functions found in counter.py + overwrite.py
# Author: Katie Mc Donald


# a function which reads from a file that exists
filename = 'count.txt'
def read_counter():
    with open(filename) as f:
        count = int(f.read())
        return count

# a function which overwrites the file with the number passed to it
filename = 'count.txt'
def overwrite_count(number):
    with open(filename, 'wt') as f:
        f.write(str(number))


num = read_counter()
# increases count
num += 1 
print('This program has been run {} times'.format(num))
overwrite_count(num)