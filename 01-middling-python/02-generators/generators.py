# String Formatting
# You can create strings by using just "string" or 'string' or '''string''' or """string""". You can
# create more dynamic or template style strings by using some placeholders and arguments using the
# .format method

full_name = 'My full name is {} {}'
print full_name

# You can use the {} as placeholders for arguments in the format method on a string.
my_full_name = full_name.format('Peter', 'Freeze')
print my_full_name

# This can cause issues though if I unknowingly switch the order of those arguments or forget
# which order they should be in.
my_full_name_two = full_name.format('Freeze', 'Peter')

# We can fix that by specifying keys to use for each placeholder which allows you to reuse or
# change the order of appearance without changing the meaning
full_name_key = 'First name: {first}, Last name: {last}, Full name: {first} {last}'
print full_name_key

# Now we can pass the arguments in any order, and because we have indicated which values should 
# be what, it doesn't matter. Also looking at the template string let's us know what values
# we should be providing
my_first_and_last = full_name_key.format(last='Freeze', first='Peter')
print my_first_and_last




# Comprehensions
# A list comprehension is a statement that creates a list in places. Rather than needing to create
# a function that can return a complete list, we can write one enclosed statement that results 
# in the same thing. We can use functions to assign a list of values to a variable
comp_one = range(10)
print comp_one

# Alternatively we could do that in-line with a comprehension like below
comp_two = [
    number for number in range(10)
]
print comp_two

# This may not seem to useful since we are currently using a function to create our list. Now let's
# make a sub list based on an initial list. Here we are creating a comprehension that is only even
# numbers.
original_range = range(100)
comp_three = [
    number  # transformation
    for number in original_range  # iteration
    if number  # condition
]
print comp_three

# You can get a lot more complicated quickly by changing the complexity of the condition or the 
# iteration item. See the example below:
comp_four = [
    c_num * num
    for num in range(20)
    for c_num in range(num)
    if not c_num % 2
]
print comp_four




# Generators
# Generators are similar to comprehensions in that they literally generate a list of things. They
# differ in powerful ways though. Compare the following output of a comprehension to a generator

comprehension = [number for number in range(10)]
print comprehension

def number_generator():
    for number in range(10):
        yield number

generator = number_generator()
print generator

# The generator has not executed anything in memory, it is still just the generator rather than the
# result of it. So given a list of 100,000 items, moving that around based on a comprehension would
# be costly, but if we set up what we need using a generator we are only moving around how to
# calculate items in the sequence instead of the calculated result

# Another part about generators is that they keep their state, compare that with a normal function
group = range(10)

def normal_fn(group=[]):
    result = 0
    for item in group:
        result = result + 1
        return result

# We expect this to be 1 since nothing was passed in, it should execute 0 + 1
print normal_fn(group)
# Same result
print normal_fn(group)

# Now let's try using the generator key word "yield"
def generator_fn(nums=[]):
    result = 0
    for num in nums:
        result = num + result + 10
        yield result

gen_one = generator_fn(group)
# You can see this has resulted in a generator
print gen_one
# Let's execute that with a for loop to see what it does differently
for number in gen_one:
    # We can see that the result is building on itself rather than reseting each time it is called
    # the result is reset in the normal_fn version, but result continues to store the last result
    # in the generator_fn version
    print number