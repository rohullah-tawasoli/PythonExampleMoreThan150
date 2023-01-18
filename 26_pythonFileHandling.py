""" Python File Handling """

# 01
# Read a file
f = open("..\PE\myFille.txt", "r")
print(f.read())

# 02
# Read only parts of a file
f = open("..\PE\myFille.txt", "r")
print(f.read(5))

# 03
# Read one line of a file
f = open("..\PE\myFille.txt", "r")
print(f.readline())

# 04
# Loop through the of a file to read the whole file, line by line
f = open("..\PE\myFille.txt", "r")
for x in f:
    print(x)