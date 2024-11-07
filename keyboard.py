# Part 2 gathers user-inputted numbers until "done" is entered
# Parameters: None (takes input from the user directly)

# Returns: A list of floats containing the valid numbers entered by the user.
# Prompts the user to enter a number, and appends valid numbers to a list.
# If "done" is entered, stops gathering inputs and returns the list.

def gather_numbers():
    users_inputs = []

    while True:
        gathering = input("Enter a number: ")
        if gathering.lower() == "done":
            break

        try:
            number = float(gathering)
            users_inputs.append(number)
        except:
            print("That number is not valid. Please enter a valid number or type done if you are finished.")

    return users_inputs

def main():
    gather_numbers()

if __name__ == '__main__':
    main()