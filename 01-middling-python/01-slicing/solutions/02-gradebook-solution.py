class GradeBook(object):
    """ Stores and retrieves grades for students. Slicing allows grades to be retrieved by a range
        of dates specified as a zero based integer for the day of the year
    """
    def __init__(self, name='Unknown Class Gradebook', grades=[]):
        """ Set a name for the grade book and the list of grades
        """
        self.name = name
        self.grades = grades

    def __getitem__(self, key):
        """ Filter grades by slicing using the start and stop properties or get one by index
        """
        if hasattr(key, 'start') and hasattr(key, 'stop'):
            # Define an empty list that we can add our results to
            grades_between_dates = []
            # Check each grade that is a member of this Gradebook
            for grade in self.grades:
                # Mimic default slice behavior of >= start and < stop
                if grade['date'] >= key.start and grade['date'] < key.stop:
                    # If it falls in the correct range, add it to the list to be returned
                    grades_between_dates.append(grade)
        else:
             self.grades[key] = self.grades[key]
        return grades_between_dates

    def add_grades(self, new_grades):
        """ Add the list of new grades to the existing list of grades
        """
        self.grades = self.grades + new_grades

# Define the list of grades to be used
raw_grades = [
    {'student_name': 'Billy', 'date': 14, 'grade': 87},
    {'student_name': 'Melissa', 'date': 14, 'grade': 90},
    {'student_name': 'Sarah', 'date': 14, 'grade': 83},
    {'student_name': 'Billy', 'date': 11, 'grade': 84},
    {'student_name': 'Melissa', 'date': 11, 'grade': 92},
    {'student_name': 'Sarah', 'date': 11, 'grade': 77},
    {'student_name': 'Billy', 'date': 23, 'grade': 89},
    {'student_name': 'Melissa', 'date': 23, 'grade': 95},
    {'student_name': 'Sarah', 'date': 23, 'grade': 80},
    {'student_name': 'Billy', 'date': 5, 'grade': 94},
    {'student_name': 'Melissa', 'date': 5, 'grade': 90},
    {'student_name': 'Sarah', 'date': 5, 'grade': 85},
]

# Create an instance of GradeBook for our math class using the grades defined above
math_class = GradeBook(name='Math GradeBook', grades=raw_grades)

# Request grades that have a "date" that falls between 1 and 9, including 1, excluding 9
print 'Request the grades from the first to the twelfth of the year:'
print math_class[0:12]

# We can add to the grades using the method we created "add_grades"
more_grades = [
    {'student_name': 'Billy', 'date': 30, 'grade': 91},
    {'student_name': 'Melissa', 'date': 30, 'grade': 86},
    {'student_name': 'Sarah', 'date': 30, 'grade': 85},
]

# Add the new grades from the list above
math_class.add_grades(more_grades)

# Check that the slice has them included
print 'Request teh new grades by selecting grades from the twenty-first to the thirtieth'
print math_class[20:31]