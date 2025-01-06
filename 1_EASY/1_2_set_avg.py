'''
Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
SOLUTION:

'''

def average(array):
    # Initialize the variable to store the sum of unique elements
    sum = 0
    
    # Use a set to remove duplicate elements from the array
    for i in set(array):
        # Add each unique element to the sum
        sum = sum + i
    
    # Calculate the average of the unique elements
    # Divide the sum by the count of unique elements
    result = sum / len(set(array))
    
    # Format the result to three decimal places and return
    return "{:.3f}".format(result)

if __name__ == '__main__':
    # Read the number of elements in the array
    n = int(input())
    
    # Read the elements of the array as a space-separated string,
    # convert them into integers, and store them in a list
    arr = list(map(int, input().split()))
    
    # Call the average function with the input array
    result = average(arr)
    
    # Print the formatted average result
    print(result)
