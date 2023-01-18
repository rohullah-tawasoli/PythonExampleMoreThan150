""" Python RegEx """

# 01
# Search a string to see if it starts with "The" and ends with "Spain"
import re
# Check if the string starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x :
    print("Yes, We have a match!")
else :
    print("No match")

# 02
# Using the findall() function
import re
# Return a list containing every occurrence of "ai"
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# 03
# Using the search() function
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position : ", x.start())

# 04
# Using the split() function
import re
# Split the string at every white-space character :
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# 05
# Using the sub() function
import re
# Replace all white-space characters with the digit "9" :
txt = "The rain in Spain"
x = re.sub("\s", "_", txt)
print(x)