""" Python Try Except """

# 01
# When an error occurs, print a message
# The try block will generate an error, because x is not defined
try :
    print(x)
except :
    print("An exception occurred")

# 02
# Many exceptions
# The try block will generate a NameError, because x is not defined :
try :
    print(x)
except NameError :
    print("Variable x is not defined")
except:
    print("Someting else went wrong")

# 03
# Use the else keyword to defined a block of code to be executed if no errors were raised
# The try block does not raise any errors, so the else block is executed :
try :
    print("Hello")
except:
    print("Someting went wrong")
else :
    print("Noting went wrong")

# 04
# Use the finally block to execute code regardless if the try block raises an error or not
# The finally block gets executed no matter if the try block raises any errors or not
try :
    print(x)
except :
    print("Someting went wrong")
finally :
    print("The 'try except' is finished")