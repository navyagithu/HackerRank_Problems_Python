''' 
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
SOLUTION:
'''
#!/bin/python3

# Import necessary libraries
import math  # Standard math library (not used in this script)
import os  # Provides functionality to interact with the operating system
import random  # For generating random numbers (not used in this script)
import re  # Regular expression library (not used in this script)
import sys  # Provides system-specific parameters and functions

# Define the solve function to capitalize each word in the input string
def solve(s):
    # Split the string by spaces, capitalize each word, and join them back with spaces
    return " ".join([i.capitalize() for i in s.split(' ')])

# Main execution starts here
if __name__ == '__main__':
    # Open a file for writing output; the file path is specified in the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Take input string from the user
    s = input()

    # Call the solve function to process the input and get the result
    result = solve(s)

    # Write the result to the output file followed by a newline
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()
