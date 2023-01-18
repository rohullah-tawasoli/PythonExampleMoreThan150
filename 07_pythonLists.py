""" Python Lists """

# 01
# Create a list
import this


thisList = ["apple", "banana", "cherry"]
print(thisList)

# 02
# Access list items
thisList = ["apple", "banana", "cherry"]
print(thisList[1])

# 03
# Change the value of a list item
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackCurrant"
print(thisList)

# 04
# Loop through a list
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# 05
# Check if a list item exists
thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

# 06
# Get the length of a list
thisList = ["apple", "banana", "cherry"]
print(len(thisList))

# 07
# Add an item to the end of a list
thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)

# 08
# Add an item at a specified index
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)

# 09
# Remove an item
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

# 10
# Remove the last item
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)

# 11
# Remove an item at a specified index
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# 12
# Empty a list
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

# 13
# Using the list() constructor to make a list
thisList = list(("apple", "banana", "cherry"))
print(thisList)