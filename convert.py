# Part 1 converts a string to a float

# Parameters:
# input_str: The string that we want to convert to a float (data type str)

# Returns: The converted float value if conversion is successful, otherwise None if the input string cannot be converted to a float.
def str_to_float(input_str: str) -> float:
    try:
        converted = float(input_str)
        return converted
    except ValueError:
        return None