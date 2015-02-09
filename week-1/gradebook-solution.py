class Gradebook(object):
    # Create a grades list on the Gradebook class (applies to every instance of Gradebook)
    grades = [
        {"value": 99, "date": 1},
        {"value": 87, "date": 2},
        {"value": 67, "date": 15},
        {"value": 91, "date": 5},
        {"value": 81, "date": 9},
        {"value": 77, "date": 12}
    ]

    def __getitem__(self, key):
        if isinstance(key, slice):
            # Empty list that we can add our results to
            grades_between_dates = []
            # Check each grade that is a member of this Gradebook
            for grade in self.grades:
                # Mimic default slice behavior of >= start and < stop
                if grade['date'] >= key.start and grade['date'] < key.stop:
                    # If it falls in the correct range, add it to the list to be returned
                    grades_between_dates.append(grade)
            return grades_between_dates
        else:
            return self.grades[key]

# Creates an instance of Gradebook
math_class = Gradebook()
# Request grades that have a "date" that falls between 1 and 9, including 1, excluding 9
print math_class[1:9]