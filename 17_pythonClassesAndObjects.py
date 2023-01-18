""" Python Classes and Objects """

# 01
# Create a class
class MyClass:
    x = 5

print(MyClass)

# 02
# Create an object
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# 03
# The __init__() Function
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

p1 = Person('John', 26)
print(p1.name)
print(p1.age)

# 04
# Create object methods
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def myFunction(self) :
        print('Hello my name is ' + self.name)

p1 = Person('John', 26)
p1.myFunction()

# 05
# The self parameter
class Person:
    def __init__(mySillyObject, name, age) :
        mySillyObject.name = name
        mySillyObject.age = age

    def myFunction(abc) :
        print('Hello my name is ' + abc.name)

p1 = Person('John', 26)
p1.myFunction()

# 06
# Modify object properties
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def myFunction(self) :
        print('Hello my name is ' + self.name)

p1 = Person('John', 26)
p1.age = 36
print(p1.age)

# 07
# Delete object properties
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def myFunction(self) :
        print('Hello my name is ' + self.name)

p1 = Person('John', 26)
del p1.age
# print(p1.age)
# Note : AttributeError => 'Person' object has no attribute 'age'

# 08
# Delete an object
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def myFunction(self) :
        print('Hello my name is ' + self.name)

p1 = Person('John', 26)
del p1
# print(p1)
# Note : NameError => name 'p1' is not defined