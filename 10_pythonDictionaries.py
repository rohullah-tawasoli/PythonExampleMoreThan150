""" Python Dictionaries """

# 01
# Create a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
print(thisDict)

# 02
# Access the items of a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
x = thisDict['model']
print(x)

# 03
# Change the value of a specific item in a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
thisDict['year'] = 2018
print(thisDict)

# 04
# Print all key names in a dictionary, one by one
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
for x in thisDict:
    print(x)

# 05
# Print all values in a dictionary, one by one
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
for x in thisDict:
    print(thisDict[x])

# 06
# Using the values() function to return values of a dictionray
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
for x in thisDict.values():
    print(x)

# 07
# Loop through both keysan values, by using the items() function
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
for x in thisDict.items():
    print(x)

# 08
# Check if a key exists
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
if 'model' in thisDict:
    print('Yes, \'model\' is one of the keys in the thisDict dictionary')

# 09
# Get the length of a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
print(len(thisDict))

# 10
# Add an item to a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
thisDict['color'] = 'red'
print(thisDict)

# 11
# Remove an item from a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
thisDict.pop('model')
print(thisDict)

# 12
# Empty a dictionary
thisDict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
thisDict.clear()
print(thisDict)

# 13
# Using the dict() constructor to create a dictionary
# Note : that keywords are not string literals
# Note : the use or equals rather than colon for the assignment
thisDict = dict (brand = 'Ford', model = 'Mustang', year = '1964')
print(thisDict)