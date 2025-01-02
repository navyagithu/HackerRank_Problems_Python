'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
SOLUTION:

'''
def split_and_join(line):
    # Splits the input string into a list of words using the default space delimiter
    line = line.split()
    # Joins the list of words into a single string, separated by hyphens
    line = "-".join(line)
    # Returns the modified string
    return line

if __name__ == '__main__':
    # Reads a line of input from the user
    line = input()
    # Calls the split_and_join function to transform the input string
    result = split_and_join(line)
    # Prints the transformed string
    print(result)
