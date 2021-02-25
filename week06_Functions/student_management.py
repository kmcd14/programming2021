# student_management.py
# This program will allow the user to create new students and view the added students
# Author: Katie Mc Donald


# title menu
def title_menu():
    print('\nWhat would you like to do?\n')
    print('\t(a) Add new student')
    print('\t(v) View Students')
    print('\t(q) Quit')
    
    choice = input('\nPlease choose a letter a/v/q to continue ')
    return choice 

# adding new student
def add(students):
    current_student = {}   #empty dict
    current_student['name'] = input('\tEnter Name: ')
    current_student['modules'] = read_modules()
     #adds new student to dict
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input('Enter the module name (blank to quit): ')
    
    while module_name != '':
        module = {}
        module['Class'] = module_name
        module['Grade'] = int(input('\tEnter grade: '))
        modules.append(module)
        module_name = input('Enter the next module name (or blank to quit): ')
   
    return modules


# viewing students

def view_modules(modules):
    print('\tClass   \t Grade')
    for module in modules:
                print('\t{}     \t {}'.format(module['Class'], module['Grade']))

def view(students):
    for current_student in students:
        print(current_student['name'])
        view_modules(current_student['modules'])


#main programme
students = [] 
choice = title_menu()
while choice != 'q':
    if choice == 'a':
        add(students)
    elif choice == 'v':
        view(students)
    elif choice == 'q':
        print('please select a,v or q \n')
    choice = title_menu()


