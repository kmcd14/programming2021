# students.py
# this program stores a students name, course and grade using dicts
# and will print out the data
# author: Katie Mc Donald

#creating the dict
#courses are a list within a dict
student = {'Name': 'Mary', 
            'Courses': [
            { 'course_name': 'Programming', 'Grade': 45 },
            {'course_name': 'History', 'Grade': 99}
            ]
            }

print('Student: {}'.format(student['Name']) )
#iterating through the courses
for course in student['Courses']:
    #prints the course and grade                   
    print('\t {} \t: {}'.format(course['course_name'], course['Grade']))