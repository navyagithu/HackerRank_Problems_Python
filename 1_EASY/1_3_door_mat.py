'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
STATUS: inprogress
LINK: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
SOLUTION:

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input().split()[0])
M = N*3
odd_positions = [i for i in range(1,N) if i%2 !=0]
for row_number in range(1,N+1):
    middle_row_number = round(N/2)
    special_symbol = '.|.'

    if row_number == middle_row_number:
        print('WELCOME'.center(M,'-'))

    else:
        if row_number < middle_row_number:
            multiple_number = odd_positions[row_number-1]
            special_symbol_mul = special_symbol*multiple_number
            print(special_symbol_mul.center(M,'-')) 

        if row_number > middle_row_number:
            multiple_number = odd_positions[(row_number-N)*-1]
            special_symbol_mul = special_symbol*multiple_number
            print(special_symbol_mul.center(M,'-'))
