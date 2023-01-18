""" Python Modules """

# 01
# 
# import myModule
# myModule.greeting('Jonatan')
# result for example => print string => Hello, Jonatan

# 02
# Variables in module
# import myModule
# a = myModule.person['age']
# print(a)
# result for example => print string => 26

# 03
# Rename a module
# import myModule as mx
# a = mx.person['age']
# print(a)
# result for example => print string => 26

# 04
# Built-in module
import platform
x = platform.system()
print(x)

# 05
# Using the dir() function
import platform
x = dir(platform)
print(x)

# 06
# import from module
# from myModule import person
# print(person['age'])
# result for example => print string => 26