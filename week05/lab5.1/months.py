#months.py
#learning about tuples
#stores the months of the year in a tuple & from this tuple creates another
#which prints out the summer months one at a time
#author: Katie Mc Donald

months = ('January', 'Febuary', 'March', 'April', 'May', 
            'June', 'July', 'August', 'September', 'October',
            'November', 'December' )


summer_months = months[4:7]
for month in summer_months:    #iterates through the months in tuple
    print(month)