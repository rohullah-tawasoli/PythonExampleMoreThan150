""" Python String """

# 01
# Get the character at position 1 of a string
a = "Hello, World!"
print(a[1])

# 02
# Substring get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

# 03
# Remove whitspace from the beginning or at the end of a string
a = " Hello, World! "
print(a.split())

# 04
# Return the length of a string
a = "Hello, World!"
print(len(a))

# 05
# Convert a string to upper case
a = "Hello, World!"
print(a.upper())

# 06
# Convert a string to lower case
b = "Hello, World!"
print(b.lower())

# 07
# Replace a string with another string
a = "Jello, World!"
print(a.replace("J", "H"))

# 08
# Split a string into substring
a = "Hello, World!"
b = a.split(",")
print(b)