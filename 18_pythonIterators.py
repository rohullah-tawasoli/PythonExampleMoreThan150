""" Python Iterators """

# 01
# Return an iterator from a tuple
myTuple = ('apple', 'banana', 'cherry')
myIterator = iter(myTuple)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# 02
# Return an iterator from a string
myString = 'banana'
myIterator = iter(myString)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# 03
# Loop through an iterator
myTuple = ('apple', 'banana', 'cherry')
for x in myTuple:
    print(x)

# 04
# Create an iterator
class MyNumbers:
    def __iter__(self) :
        self.a = 1
        return self

    def __next__(self) :
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIterator = iter(myClass)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# 05
# Stop iteration
class MyNumbers:
    def __iter__(self) :
        self.a = 1
        return self

    def __next__(self) :
        if self.a <= 20 :
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = MyNumbers()
myIterator = iter(myClass)
for x in myIterator:
    print(x)