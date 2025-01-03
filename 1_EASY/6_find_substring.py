'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
SOLUTION:
'''

def count_substring(string, sub_string):
    # Initialize a counter to keep track of the occurrences of the substring
    count = 0
    # Iterate through each character in the string
    for i in range(len(string)):
        # Check if the slice of the string starting at the current index
        # and having the length of the substring matches the substring
        if string[i:i+len(sub_string)] == sub_string:
            # If there's a match, increment the counter
            count = count + 1
    # Return the total count of substring occurrences
    return count

if __name__ == '__main__':
    # Read the main string from the user, removing any extra spaces
    string = input().strip()
    # Read the substring from the user, removing any extra spaces
    sub_string = input().strip()
    
    # Call the function to count the occurrences of the substring in the main string
    count = count_substring(string, sub_string)
    # Print the result
    print(count)
