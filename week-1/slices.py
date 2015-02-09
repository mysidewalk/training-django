# Slices are a way of splitting or extracting a set portion of "list". Things that can be sliced
# normally include: Lists, Tuples, Strings.

names = ['Kevin', 'Bob', 'Joey', 'Michael', 'Matthew']

# We can split this list using the slice syntax of: [start:stop:step]. Start is the 0 based index
# which the sliced set will include, stop is the index of the first item NOT included. Stop is an 
# up-to value. Step is the indicator for direction and length, allowing you to include every other,
# every other reverse etc.

sliced_names = names[0:2]
print sliced_names


# You can create a slicing object with the same three values. The declaration
# below creates a sliced subset just like the above syntax

to_slice = 'platform intermediate'
slice_result = to_slice[0:8:-1]
print slice_result


# You can make slices more complex and powerful by changing how an object responds to a slice.
# Things that we would often considering needing a subset of is data, organized by a date. 
# Slicing uses the double under method __getitem__(self, slice_value):
# Write a __getitem__ method that allows you to specify the string version of indexes
# (e.g. "zero" instead of "0"). (Don't worry about implementing support for negative numbers)

class StringSlice(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, value):
        # Update this method to translate string values into integers that it can use to slice
        # self.name if value is a slice
        pass

string_slice = StringSlice('MindMixer')
result = string_slice['one':'three']
# Should print the letters 1-2
print result


class Gradebook(object):
    grades = [
        {"value": 99, "date": 1},
        {"value": 87, "date": 2},
        {"value": 67, "date": 15},
        {"value": 91, "date": 5},
        {"value": 81, "date": 9},
        {"value": 77, "date": 12}
    ]

    def __getitem__(self, key):
        # Put your solution here for returning the proper subset of grades based on if they fall
        # between the start and stop values.

math_class = Gradebook()
# Should return the grades for any grade with a "date" value between 1 and 9, including 1 and 
# excluding 9.
print math_class[1:9]