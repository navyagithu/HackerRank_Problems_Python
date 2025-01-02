''' 
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer n at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
SOLUTION:
'''
if __name__ == '__main__':
    # Read the number of operations to be performed
    N = int(input())
    
    # Initialize an empty list to perform operations on
    list1 = []
    
    # Loop through the number of operations
    for _ in range(N):
        # Read and split the input to identify the operation and its arguments
        oper_list = input().split()
        
        # Check the operation type and perform accordingly
        if oper_list[0] == "insert":
            # 'insert' operation: Add the value at the specified index
            index = int(oper_list[1])
            value = int(oper_list[2])
            list1.insert(index, value)
        
        if oper_list[0] == "print":
            # 'print' operation: Print the current state of the list
            print(list1)
        
        if oper_list[0] == "remove":
            # 'remove' operation: Remove the first occurrence of the specified value
            value = int(oper_list[1])
            list1.remove(value)
        
        if oper_list[0] == "append":
            # 'append' operation: Add the value to the end of the list
            value = int(oper_list[1])
            list1.append(value)
        
        if oper_list[0] == "sort":
            # 'sort' operation: Sort the list in ascending order
            list1.sort()
        
        if oper_list[0] == "pop":
            # 'pop' operation: Remove the last element from the list
            list1.pop()
        
        if oper_list[0] == "reverse":
            # 'reverse' operation: Reverse the order of elements in the list
            list1.reverse()
