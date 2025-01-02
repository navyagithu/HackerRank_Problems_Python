'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
SOLUTION:
'''
# This is the main block of the program
if __name__ == '__main__':
    # Read an integer input from the user, representing the number of elements in the list
    n = int(input())
    
    # Read a space-separated list of integers from the user and map them to a list of integers
    integer_list = map(int, input().split())
    
    # Convert the list of integers to a tuple and compute its hash value
    # The hash function returns an integer hash value for the tuple
    print(hash(tuple(integer_list)))
