""" Python JSON """

# 01
# Convert from JSON to Python
import json
# some JSON
x = '{"name" : "John", "age" : 26, "city" : "New Yourk"}'
# parse x :
y = json.loads(x)
# the result is a Python dictionary :
print(y["age"])

# 02
# Convert from Python to JSON
import json
# a python object (dict) :
x = {
    "name" : "John",
    "age" : 26,
    "city" : "New Yourk"
}
# convert into JSON :
y = json.dumps(x)
# the result is a JSON string :
print(y)

# 03
# Convert Python objects into JSON strings
import json
print(json.dumps({"name" : "John", "age" : 6, "city" : "New Yourk"}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("Hello"))
print(json.dumps(26))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# 04
# Convert a Python object containing all the legal data types
import json
x = {
    "name" : "John",
    "age" : 26,
    "married" : True,
    "divorced" : False,
    "childern" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        { "model" : "BMW", "mpg" : 27.5 },
        { "model" : "Ford Edge", "mpg" : 24.1 }
    ],
    "city" : "New Yourk"
}
# convert into JSON :
y = json.dumps(x)
# the result is a JSON string :
print(y)

# 05
# Use the indent parameter to define the numbers of indents
import json
x = {
    "name" : "John",
    "age" : 26,
    "married" : True,
    "divorced" : False,
    "childern" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        { "model" : "BMW", "mpg" : 27.5 },
        { "model" : "Ford Edge", "mpg" : 24.1 }
    ],
    "city" : "New Yourk"
}
# use four indents to make it easier to read the result :
print(json.dumps(x, indent = 4))

# 06
# Use the separators parameter to change the default separator
import json
x = {
    "name" : "John",
    "age" : 26,
    "married" : True,
    "divorced" : False,
    "childern" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        { "model" : "BMW", "mpg" : 27.5 },
        { "model" : "Ford Edge", "mpg" : 24.1 }
    ],
    "city" : "New Yourk"
}
""" use and a space to separate objects, and a space, a = and a space to separate
    keys from their values :
""" 
print(json.dumps(x, indent = 4, separators = (" ", " = ")))

# 07
# Use the sort_keys parameter to specify if the result should be sorted or not
import json
x = {
    "name" : "John",
    "age" : 26,
    "married" : True,
    "divorced" : False,
    "childern" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        { "model" : "BMW", "mpg" : 27.5 },
        { "model" : "Ford Edge", "mpg" : 24.1 }
    ],
    "city" : "New Yourk"
}
# sort the result alphabetically by keys :
print(json.dumps(x, indent = 4, separators = (" ", " = "), sort_keys = True))