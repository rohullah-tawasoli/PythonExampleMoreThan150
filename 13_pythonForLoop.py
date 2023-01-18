""" Python For Loop """

# 01
# The for loop
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# 02
# Loop through a string
for x in 'banana':
    print(x)

# 03
# Using the break statement in a for loop
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# 04
# Using the continue statement in a for loop
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# 05
# Using the range() function in a for loop
for x in range(6):
    print(x)

# 06
# Else in for loop
for x in range(6):
    print(x)
else: print('Finally finished')

# 07
# Nested for loop
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)