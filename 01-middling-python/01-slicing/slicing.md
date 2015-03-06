## Python Slicing

### Preparation
- [Python's magic methods](http://www.rafekettler.com/magicmethods.html)
- [Conceptual explination of slicing](http://stackoverflow.com/questions/509211/explain-pythons-slice-notation/509295#509295)
- [Slicing in practice](http://www.diveintopython.net/native_data_types/lists.html#odbchelper.list.slice)

### Exercises
1. Create a class called `SliceByString` that allows slicing using strings for integers 1-9 (e.g.
    'one' for 1). (Don't worry about negative values for this exercise)
    - Define a new class, along with `__init__` and `__getitem__` methods
    - The `__init__` method should accept at least 1 parameter that is a list, and store it on the
        class as an instance based variable
    - You should create a mapping of strings to integers as a class based property for the integers
        0 through 9
    - You should only modify the slicing behavior, not the retrieving of a value from the list by
        index

2. Create a class called `GradeBook` that overrides allows for slicing based on the date a grade
    was entered into the GradeBook (For this exercise, assume dates are integers according to 
    the day of the year, e.g. January 1 would be 0, Jaunary 2, would be 1)
    - Customize the slicing behavior to return all of the grades that fall between the dates
        provided (Keep to normal slicing sytax; [start:stop] where stop represents up to that index)
    - Your GradeBook class should also provide a method to add to the set of grades
    - A single grade should have the following properties: student_name, date (which should be an integer),
        and grade

#### Links
Next: [List Comprehensions and Generators](../02-generators/generators.md)
