# json_dict.py
# This program contains a function which will store a dict to a file as JSON
# Author: Katie Mc Donald

import json

filename = 'testdict.json'
sample = dict(name='Gillian', age='45', grades=[1, 34, 55])

def write_dict(object):
    with open(filename, 'wt') as f:
        json.dump(object, f)

write_dict(sample)