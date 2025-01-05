'''
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
SOLUTION:
'''
def wrap(string, max_width):
    # Initialize an empty list to store substrings
    list1 = []
    
    # Loop through the string in steps of max_width
    for i in range(0, len(string), max_width):
        # Append each substring of length max_width to the list
        list1.append(string[i:i+max_width])
    
    # Join the substrings in the list with a newline character and return the result
    return "\n".join(list1)

if __name__ == '__main__':
    # Take the input string and the maximum width for wrapping
    string, max_width = input(), int(input())
    
    # Call the wrap function to get the wrapped string
    result = wrap(string, max_width)
    
    # Print the resulting wrapped string
    print(result)
