# normalise.py
# this program reads a string and strips any leading or trailing spaces
# it will also convert the string to lowercase 
# and output the lenght of both the orginal and new string
# author: Katie Mc Donald

org_string = input('please enter a string: ')
new_string = org_string.strip().lower()

lenght_of_org = len(org_string)
lenght_of_new = len(new_string)

print('The orginal string was: {}\nWe have normalised it to: {}'.format(org_string, new_string))
print('We have reduced the lenght of the orignal string from {} to {}'.format(lenght_of_org, lenght_of_new))