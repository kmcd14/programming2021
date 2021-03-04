# read_dict.py
# A function which will read in a dict object from a file
# Author: Katie Mc Donald

import json

filename = 'test_dict.json'

def read_dict():
    with open(filename) as f:
        return json.load(f)

some_dict = read_dict()
print(some_dict)