""" Python Functions """

# 01
# Create and call a function
def myFunction():
    print('Hello from a function')

myFunction()

# 02
# Function parameters
def myFunction(fname):
    print(fname + ' Refsnes')

myFunction('Emil')
myFunction('Tobias')
myFunction('Linus')

# 03
# Default parameter value
def myFunction(country = 'Norway'):
    print('I am from ' + country)

myFunction('Sweden')
myFunction('India')
myFunction()

# 04
# Let a function return a value
def myFunction(x):
    return 5 * x

print(myFunction(3))
print(myFunction(5))
print(myFunction(9))

# 05
# Recursion
def triRecursion(k):
    if (k > 0):
        result = k + triRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('\n\nRecursion Example Results') 
triRecursion(6)