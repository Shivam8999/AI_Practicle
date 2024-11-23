# Write a Python program to accept a string. Find and print the number of upper case alphabets
# and lower case alphabets.
def count_case_characters(input_string):
    # Initialize counters for uppercase and lowercase letters
    upper_case_count = 0
    lower_case_count = 0
    for char in input_string:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1

    # Print the results
    print("Number of uppercase letters:", upper_case_count)
    print("Number of lowercase letters:", lower_case_count)

# Accept a string from the user
user_input = input("Enter a string: ")

# Call the function with the user input
count_case_characters(user_input)
