'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
SOLUTION:

'''
def swap_case(s):
    # Initialize an empty string to store the result
    output = ""
    
    # Iterate through each character in the input string
    for i in s:
        # Check if the character is in uppercase
        if i == i.upper():
            # Convert uppercase to lowercase and add to the output string
            output = output + i.lower()
        # Check if the character is in lowercase
        elif i == i.lower():
            # Convert lowercase to uppercase and add to the output string
            output = output + i.upper()
        else:
            # If the character is neither uppercase nor lowercase (e.g., digit or special character),
            # append it to the output string unchanged
            output = output + i
            
    # Return the modified string with cases swapped
    return output

if __name__ == '__main__':
    # Take input from the user
    s = input()
    # Call the swap_case function to transform the string
    result = swap_case(s)
    # Print the transformed string
    print(result)
