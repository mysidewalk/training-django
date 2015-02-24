# See W1D1.md for the exercise prompt

class StringSlice(object):
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

    # Set the init function to accept a name and a default value of 'MindMixer' if it is not provided
    def __init__(self, name='MindMixer'):
        self.name = name

    def __getitem__(self, key):
        start = 0
        stop = 0
        step = 1
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
string_slice = StringSlice('MySidewalk')
print string_slice['zero':'three']
