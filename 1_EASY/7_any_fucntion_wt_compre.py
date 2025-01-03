'''
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
SOLUTION:
'''



# Main block of the script
if __name__ == '__main__':
    # Take input string from the user
    s = input()

    # Check if there is any alphanumeric character in the string and print the result
    # `isalnum()` checks if the character is alphanumeric (letters or digits)
    print(any([True if i.isalnum() else False for i in s.split()]))
        
    # Check if there is any alphabetical character in the string and print the result
    # `isalpha()` checks if the character is an alphabet
    print(any([True if i.isalpha() else False for i in s ]))
    
    # Check if there is any digit in the string and print the result
    # `isdigit()` checks if the character is a digit
    print(any([True if i.isdigit() else False for i in s]))
    
    # Check if there is any lowercase letter in the string and print the result
    # `islower()` checks if the character is a lowercase letter
    print(any([True if i.islower() else False for i in s ]))
    
    # Check if there is any uppercase letter in the string and print the result
    # `isupper()` checks if the character is an uppercase letter
    print(any([True if i.isupper() else False for i in s]))
