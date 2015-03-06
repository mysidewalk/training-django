PRINT_OUTPUT = True

## Slicing
# Slicing is a way of splitting or extracting a set portion of "list". Types that can be sliced by
# default include: Lists, Tuples, Strings. Below is a list of names, we will use slices to grab
# only a subset of that.
names = ['Kevin', 'Bob', 'Joey', 'Michael', 'Matthew']

# We can slice this list using the syntax of: "[start:stop:step]". Start is the 0 based index
# which the sliced set will include, stop is the index of the first item NOT included. Stop is an 
# up-to value. Step is the indicator for direction and length, allowing you to include every other,
# every third in reverse etc. Slicing returns the subset in a new list so it the result can be 
# assigned to a new variable.

# Breaking down the syntax, the following slice is:
# Start is set to 0, so we expect the first item of the list to be included
# Stop is set to 2, so we should not expect to see the third item (indexes start at 0) but it should
#    include the second since stop includes everything up to that index.
# Step is not provided which means it defaults to 1, meaning it will go through each one rather than
#    skipping over some
sliced_names = names[0:2]
if PRINT_OUTPUT:
    print sliced_names

# You can create a slicing object with the same three values of start, stop, step. Using the slicing
# syntax or slice object constructor are both valid.
label = 'Platform Intermediate'
slice_for_label = slice(0, 8)
sliced_label = label[slice_for_label]
if PRINT_OUTPUT:
    print sliced_label

# When a List is sliced in Python it calls a "magic method"; __getitem__(). This method has two
# params, self, a reference to the object it was called on and key. Default behavior expects a 
# Integer or Slice object. The example below is what happens when using the normal or above syntax.
teams = ['Participant', 'Data', 'Organizations', 'Shared']
slice_for_teams = slice(1, 4)
sliced_teams = teams.__getitem__(slice_for_teams)
if PRINT_OUTPUT:
    print sliced_teams

# Below is an example of a class that overrides the __getitem__ method. It is important to
# understand that things besides slices also leverage this method. Unless you intend to eliminate 
# that other functionality you should be clear on when you apply that custom functionality.
# You can see in the example below that asking for an index of the list and slicing the list both
# print out the type that called __getitem__ with.
class list(list):
    """ An example that prints out the value of the "key" param for __getitem__ to illustrate that
        multiple methods rely on it
    """

    def __getitem__(self, key):
        print 'Param key is {}'.format(str(type(key)))
        return super(list, self).__getitem__(key)

numbers = list([10, 11, 12, 13, 14, 15])
slice_for_numbers = slice(0, 3)
if PRINT_OUTPUT:
    print numbers[1]
    print numbers[slice_for_numbers]

# You can create more complex functionality by simply overriding the __getitem__ method. For example
# you could create a class that expects dates for the start and stop and a week step. The class 
# could then filter the data by the dates and jump from week to week. Slices simply offer a powerful
# way to find a subset of data ordered by any attribute you deem necessary. Try the exercises now
