# *args & **kwargs
# https://freepythontips.wordpress.com/2013/08/04/args-and-kwargs-in-python-explained/

# Python has some great flexibility in calling functions with an assortment of arguments. Most
# functions you write have a set of arguments that you need and you have to place them in a specific
# order.
def fn_one(arg1, arg2, arg3):
    print arg1
    print arg2
    print arg3

print "Calling fn_one()"
fn_one(1, 2, 3)

# Calling "fn_one" with all of the arguments means you need to pass them one at a time in the right
# order. "*args" allows you to include an additional list of unknown length to the function, which
# by convention should come after your "formal arguments" or explicitly named ones.
def fn_two(arg1, arg2, *args):
    print arg1
    print arg2
    for arg in args:
        print arg

print "\n"
print "Calling fn_two()"
fn_two(1, 2, 3, 4, 5, 6)

# We can iterate through the list of *args like any other list! Optionally, **kwargs let you key
# specific values without needing them to be defined in the formal arguments list:
def fn_three(arg1, *args, **kwargs):
    print arg1
    for arg in args:
        print arg
    for key, value in kwargs.iteritems():
        print key, value

print "\n"
print "Calling fn_three()"
fn_three(1, 2, 3, 4, five=5, six=6, seven=7)