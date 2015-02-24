# Problem 1 from W1D2

# Defining a generator with an optional argument of limit
def generate_fibonacci(limit=None):
    # The generator needs two variables to hold onto the current and previous values
    previous_value = 0
    current_value = 1
    # The sequence starts with 0 and 1 so yield those first
    yield previous_value
    yield current_value
    # Continue forever
    while True:
        # Multiple variable assignment: previous_value is now current_value and current_value
        # is now previous_value + current_value
        previous_value, current_value = current_value, previous_value + current_value
        # If we had a limit and have not exceeded it yield
        if limit and current_value < limit:
            yield current_value
        # If did not have a limit yield
        elif not limit:
            yield current_value
        # Else break (limit was exceed or the world ended)
        else:
            break

limit = 1000000
print('Print Fibonacci up to {}'.format(limit))
fib = generate_fibonacci(limit)
for item in fib:
    print(item)