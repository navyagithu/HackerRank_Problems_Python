''' 
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
STATUS: SOLVED
LINK: 
SOLUTION: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
'''
def solve(s):
    # Split the string by spaces, capitalize each word, and join them back with spaces
    return " ".join([i.capitalize() for i in s.split(' ')])

# Main execution starts here
if __name__ == '__main__':
    # Take input string from the user
    s = input()

    # Call the solve function to process the input and get the result
    result = solve(s)
    print(result)