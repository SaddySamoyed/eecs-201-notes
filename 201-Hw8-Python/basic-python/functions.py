
def lower_list(input_str):
    """Returns a list of the string’s characters that are lowercase."""
    return [char for char in input_str if char.islower()]

def list_to_string_dict(input_list):
    """Returns a dict made up of the key-value pairs in the input list that have keys that are strings."""
    return {key: value for key, value in input_list if type(key) is str}

if __name__ == '__main__':
    # Example test cases for lower_list function
    print(lower_list("HelLo"))  # Expected: ['e', 'l', 'o']

    # Example test cases for list_to_string_dict function
    print(list_to_string_dict([('hello', 1), ('world', 42), (1234, 5)]))  # Expected: {'hello': 1, 'world': 42}