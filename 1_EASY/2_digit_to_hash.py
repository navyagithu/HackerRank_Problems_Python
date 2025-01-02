'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
SOLUTION:
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
