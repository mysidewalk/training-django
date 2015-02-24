# Problem 2 from W1D2

sample_dicts = {
    'a': {'a': 1, 'b': 2, 'c': 3},
    'b': {'a': 4, 'b': 5, 'c': 6},
    'c': {'a': 7, 'b': 8, 'c': 9},
}

# Defining a generator with an optional argument of limit
def generate_solution(dict_to_flatten):
    # For parent key, parent value in the dictionary
    for p_key, p_val in dict_to_flatten.items():
        # For child key, child value in parent value dictionary
        for c_key, c_val in p_val.items():
            # Yield [_._] parent key + child key = child value
            yield '{}.{}'.format(p_key, c_key), c_val

# Print the result of calling this
print dict(generate_dict(sample_dicts))
