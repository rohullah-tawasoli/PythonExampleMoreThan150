""" Python Sets """

# 01
# Create a set
from operator import le


thisSet = {"apple", "banana", "charry"}
print(thisSet)
""" Note: the set list is unordered
meaning => the items will appear in a random order."""

# 02
# Loop through a set
thisSet = {"apple", "banana", "charry"}
for x in thisSet:
    print(x)

# 03
# Check if an item exists
thisSet = {"apple", "banana", "charry"}
print("banana" in thisSet)

# 04
# Add multiple items to a set
thisSet = {"apple", "banana", "charry"}
thisSet.update(["orange", "mango", "grapes"])
print(thisSet)

# 05
# Get the length of a set
thisSet = {"apple", "banana", "charry"}
print(len(thisSet))

# 06
# Remove an item in a set
thisSet = {"apple", "banana", "charry"}
thisSet.remove("banana")
print(thisSet)

# 07
# Remove an item in a set by using the discard() method
thisSet = {"apple", "banana", "charry"}
thisSet.discard("banana")
print(thisSet)

# 08
# Remove the last in a set by using the pop() method
thisSet = {"apple", "banana", "charry"}
x = thisSet.pop()
# removed item
print(x)
# the set after removal
print(thisSet)

# 09
# Empty a set
thisSet = {"apple", "banana", "charry"}
thisSet.clear()
print(thisSet)

# 10
# Delete a set
thisSet = {"apple", "banana", "charry"}
del thisSet
# this will raise an error because the set no longer exists
# print(thisSet)

# 11
# Using the set() construction to create a set
thisSet = set(("apple", "banana", "charry"))
print(thisSet)
""" Note: the set list is unordered,
so the result will display the items in a random order."""