## List Comprehensions and Generators

### Preparation
- [Generators explained](http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
- [Generator docs](https://docs.python.org/2/reference/expressions.html#generator-expressions)
- [Generator expressions](http://anandology.com/python-practice-book/iterators.html#generator-expressions)
- [Generator PEP](https://www.python.org/dev/peps/pep-0289/)

### Exercises
We are working out of [generators.py](generators.py)

1. Write a generator function that can efficiently calculate an infinite sequence
    of numbers in the Fibonacci series. Optionally allow that generator to take a limit that it will
    stop at if the next number is greater than the supplied limit.
2. Give a dictionary of dictionaries, use a nested generator expressions to transform it into
    a dictionary using the parent's key for the name space. E.g. `old_dictionary['a']['a']` would be
    set at `new_dictionary['a.a']` with the proper value

#### Links
Next: [File Operations and OS](../03-files-and-os/file-operations.md)