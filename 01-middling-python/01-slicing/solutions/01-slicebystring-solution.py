class SliceByString(object):
    """ Allows use of slicing syntax using the string equivalent of a integer, e.g. 'one' instead
        of 1, 'two' instead of 2, etc.
    """
    # Define a mapping of string words to the integer counter parts for 0-9
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    def __init__(self, name='MindMixer'):
        """ Accepts a name and sets a default value of 'MindMixer' if it is not provided
        """
        self.name = name

    def __getitem__(self, key):
        start = 0
        stop = 0
        step = 1

        # Only applying our logic if the __getitem__ is called with a slice object
        if isinstance(key, slice):
            # Check the number_map for the equivalent for start and stop
            if key.start:
                start = self.number_map[key.start]
            if key.stop:
                stop = self.number_map[key.stop]
            if key.step:
                step = self.number_map[key.step]
        # Return the sliced string based on the integer equivalents
        return self.name[start:stop:step]

# Create a StringSlice
slice_by_string = SliceByString('MySidewalk')
print slice_by_string['zero':'three']
