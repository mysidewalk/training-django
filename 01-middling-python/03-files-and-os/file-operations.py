# Get Help
# When interacting with Python in a shell or terminal environment there are always a couple ways 
# you can ask for more information. There are two major functions that help list out different
# methods and properties of a Class

# dir()
# Use dir() on any class for a alphabetized list of properties and methods that are available.

# Here we can see a quick example given a normal class with one method; "my_first_method".
class MysteryClass(object):
    """The doc string for MysteryClass"""
    def my_first_method(self):
        """The doc string for my_first_method"""
        pass

# Look at the output below by running this file in your terminal.
# The dir() statement has printed out all of the default properties/methods that a new Class 
# contains as well as our custom method. This is a great way to explore what kind of API a given
# class has.
print "Calling dir(MysteryClass)"
# print dir(MysteryClass)


# help()
# Help can be a great way of seeing a little more context than dir(). It will give you a snapshot
# of the actual definition of the Class rather than a list of properties / methods.

# Help is best used in an interactive environment like a terminal. You can see a working skeleton
# of the class / object and any comments that are also provided along with it.
print "\n"
print "Calling help(MysteryClass)"
# print help(MysteryClass)



# Tuples
# Tuples are a type of list, although they have some very important differences. Tuples can be
# created by setting a comma separated list between parenthesis.
tuple_one = (1, 2, 3)

print "\n"
print "Tuples"
print type(tuple_one)

# Tuples are immutable, they cannot be change once created. Although you can extract and modify
# different values.
# See the example below.
# tuple_two = tuple_one.append(4)

# The above example results in a TypeError. But I can still access the information stored at each
# index of a tuple.
part_one = tuple_one[0]

print "\n"
print "The first item in the tuple"
print part_one

# We can create or modify a tuple, by assigning out the values we want, and creating a new tuple
# with additional or fewer items. I can also assign more than one value at a time using tuples.
# "first" takes on the value of the item in index 0 and "second" takes on the value of item at 
# index 1.
first, second = (1, 2)
tuple_two = (first, second, 3)
print "\n"
print "Multi variable assignment with tuples"
print tuple_two

# If I have a function that needs to return more than one value, I don't have to do that with a 
# object, I can instead just return a comma separated list of values.
def multiple_return_values():
    return 1, 2, 3

print "\n"
print "Multiple return values"
print multiple_return_values()

# I can also grab each one of those return values individually with different variables. Each one of
# my variables is now mutable rather than storing the single grouping of the return as an tuple
# which is immutable.
one, two, three = multiple_return_values()
print "\n"
print "Multiple variable assignment on return"
print one, two, three



# OS
# The os provides a lot of ways that we can interact with files, folders, and many os level items, 
# which makes sense. Try using help() or dir() to explore the os object and see what kind of 
# information you can request or modify.
from platform import os

# For example we can check who is logged in currently
print "\n"
print "Check logged in user from os"
print os.getlogin()

# Codeacademy I/O
# Let's go through lessons 1-9 of this course
# http://www.codecademy.com/courses/python-intermediate-en-OGNHh/0/1



# Path
# Path is an object that has a lot of capabilities to read and write files and folders. We can read
# through a directory and find all of its files or folders, and look at properties of them as well.
# If it isn't already installed we can use "sudo pip install path.py" to install it
from path import Path

downloads = Path('/Users/peterfreeze/downloads')

print "\n"
print "Path: Images in downloads"
for image in downloads.files('*.tif'):
    print image.name, image.getsize()
