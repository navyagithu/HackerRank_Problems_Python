'''
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
SOLUTION:
'''

def mutate_string(string, position, character):
    # Create a new string by slicing the input string up to the given position,
    # adding the new character, and then appending the rest of the string after the position.
    new = string[:position] + character + string[position + 1:]
    return new

if __name__ == '__main__':
    # Take the input string from the user.
    s = input()
    
    # Take the position (as an integer) and the character from the user.
    i, c = input().split()
    
    # Call the mutate_string function with the input string, position, and character.
    s_new = mutate_string(s, int(i), c)
    
    # Print the mutated string as the output.
    print(s_new)
