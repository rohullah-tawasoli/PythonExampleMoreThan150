""" Python Dates """

# 01
# import the datetime module and display the current date
import datetime
x = datetime.datetime.now()
print(x)

# 02
# Return the year and name of weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))

# 03
# Create a date object
import datetime
x = datetime.datetime(2020, 5, 17, 12, 23, 40)
print(x)

# 04
# The strftime() Method
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime('%B'))