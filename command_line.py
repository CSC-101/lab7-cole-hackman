# Part 3 sums command-line arguments if they are valid numbers
# Parameters: None

# Returns: None (prints the total sum of all valid numeric command-line arguments)
# Loops through command-line arguments and converts each valid one to a float.
# Adds valid arguments to a sum and ignores invalid ones.

import sys

def main():
    total_sum = 0.0
    for arguments in sys.argv[0:]:
        try:
            total_sum += float(arguments)
        except:
            pass
    print("Sum of valid arguments is: ", total_sum)

if __name__ == '__main__':
    main()