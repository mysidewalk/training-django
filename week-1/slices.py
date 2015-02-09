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
slice_object = slice(0, 8, -1)
slice_result = to_slice[slice_object]
print slice_result


# You can make slices more complex and powerful by changing how an object responds to a slice.
# Things that we would often considering needing a subset of is data, organized by a date. 
# Slicing uses the double under method __getitem__(self, slice_value):
# Write a __getitem__ method that allows you to specify the string version of indexes
# (e.g. "zero" instead of "0"). (Don't worry about implementing support for negative numbers)

class StringSlices(Object):
  __init__(self, *args, **kwargs):
    pass

  __getitem__(self, value):
    # Implement your solution here
    pass