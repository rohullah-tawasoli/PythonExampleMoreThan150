""" Python Tuples """

# 01
# Create a tuple
thisTuple = ("apple", "banana", "Cherry")
print(thisTuple)

# 02
# Access tuple items
thisTuple = ("apple", "banana", "Cherry")
print(thisTuple[1])

# 03
# Change tuple values
thisTuple = ("apple", "banana", "Cherry")
# thisTuple[1] = "blackCurrant"
# the value is still the same
print(thisTuple)

# 04
# Loop through a tuple
thisTuple = ("apple", "banana", "Cherry")
for x in thisTuple:
    print(x)

# 05
# Check if a tuple item exists
thisTuple = ("apple", "banana", "Cherry")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the fruits tuple")

# 06
# Get the lenght of a tuple
thisTuple = ("apple", "banana", "Cherry")
print(len(thisTuple))

# 07
# Delete a tuple
thisTuple = ("apple", "banana", "Cherry")
del thisTuple
# this will raise an error because the no loger exists
# print(thisTuple)

# 08
# Using the tuple() construction to create a tuple
thisTuple = tuple(("apple", "banana", "Cherry"))
print(thisTuple)