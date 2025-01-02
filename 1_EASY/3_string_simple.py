'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
SOLUTION: is as below
'''

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # This function takes two parameters: first and last names.
    # It prints a formatted greeting message including the full name.
    print(f"Hello {first} {last}! You just delved into python.")  # Using an f-string to format the output message.
    
if __name__ == '__main__':
    # The following block runs only when the script is executed directly (not imported as a module).
    first_name = input()  # Prompt the user to enter their first name and store it in the variable 'first_name'.
    last_name = input()   # Prompt the user to enter their last name and store it in the variable 'last_name'.
    print_full_name(first_name, last_name)  # Call the print_full_name function with the provided names.
