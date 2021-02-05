# normalise.py
# this program reads a string and strips any leading or trailing spaces
# It will also convert the string to lowercase 
# and output the lenght of both the orignal and output sting
# author: Katie Mc Donald

raw_string = input(('please enter a string: '))
new_string = raw_string.strip().lower()

lenght_raw_string = len(raw_string)
lenght_new_string = len(new_string)

print('The string normalised is: {}'.format(new_string))
print('We reduced the input string from {} to {} characters'.format(lenght_raw_string, lenght_new_string))

