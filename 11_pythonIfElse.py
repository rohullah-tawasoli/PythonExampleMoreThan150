""" Python If ... Else """

# 01
# The if statement
a , b = 33 , 200
if b > a :
    print('b is greater than a')

# 02
# The elif statement
a, b = 33, 33
if b > a :
    print('b is greater than a')
elif a == b :
    print('a and b are equal')

# 03
# The else statement
a, b = 200, 33
if b > a :
    print('b is greater than a')
elif a == b :
    print('a and b are equal')
else:
    print('a is greater than b')

# 04
# Short hand if
a, b = 200, 33
if a > b : print('a is greater than b')

# 05
# Short hand if ... else
a, b = 2, 330
print('A') if a > b else print('B')

# 06
# The and keyword
a, b, c = 200, 33, 500
if a > b and c > a :
    print('Both conditions are True')

# 07
# The or keyword
a, b, c = 200, 33, 500
if a > b or a > c :
    print('At last one of the conditions is True')