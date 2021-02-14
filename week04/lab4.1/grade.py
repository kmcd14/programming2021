# grade.py
# this program reads a students percentage mark and prints out the corresponding grade
# author: Katie Mc Donald


percentage = float(input("Please enter the student's percentage mark: "))

# Error handling that the number entered is valid
if (percentage < 0) or (percentage > 100):
    print('Please enter a number between 0 and 100')

if percentage < 40 :  #less than 40
    print('Fail')
elif percentage < 50:  #between 40 and 49
    print('Pass')
elif percentage < 60:  #between 50 and 59
    print('Merit 2')
elif percentage < 70:  #between 60 and 69
    print('Merit 1')
else:
    print('Distinction')  #only other option is between 70 and 100