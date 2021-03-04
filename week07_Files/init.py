# init.py
# this program initialises a file
# author: Katie Mc Donald

import os.path
filename = 'count.txt'
if not os.path.isfile(filename):
    print('File does not exist')
    

def read_counter():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0