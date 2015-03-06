class SliceByString(object):
    """ Allows use of slicing syntax using the string equivalent of a integer, e.g. 'one' instead
        of 1, 'two' instead of 2, etc.
    """
    # Define a mapping of strings to integers as a class level attribute for zero to nine
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

    # Override the init method and use the kwarg "name" to set a string that will be sliced as an
    # instance property
    def __init__(self, name='MindMixer'):
        """ Accepts a name and sets a default value of 'MindMixer' if it is not provided
        """
        self.name = name

    # Override the getitem method 
    def __getitem__(self, key):
        final_value = None
        start = 0
        stop = 0
        step = 1

        # Only applying our logic if the __getitem__ is called with a slice object, since normal 
        # syntax doesn't actually identity itself as a type of slice, we will check for the
        # properties we want to use on the key object
        if hasattr(key, 'start') and hasattr(key, 'stop'):
            # Check the number_map for the equivalent for start and stop
            if key.start:
                start = self.number_map[key.start]
            if key.stop:
                stop = self.number_map[key.stop]
            if key.step:
                step = self.number_map[key.step]
            final_value = self.name[start:stop:step]
        # If not slice-like apply the normal syntax to the name property and let the string's 
        # default behavior do the work
        else:
            final_value = self.name[key]

        # Return either the custom slice or the value at the index
        return final_value

# Create a SliceByString
slice_by_string = SliceByString('MySidewalk')
print 'Result from custom slicing using "zero" and "three"'
print slice_by_string['zero':'three']
print 'Result from normal index of zerio'
print slice_by_string[0]
