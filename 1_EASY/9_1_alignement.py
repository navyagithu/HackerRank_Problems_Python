'''
Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

STATUS: SOLVED
LINK: https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
SOLUTION:
'''

# Replace all ______ with rjust, ljust, or center.

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
# Creates the cone-shaped pattern at the top of the design.
for i in range(thickness):
    # The left part of the cone (right-aligned) + center 'H' + right part of the cone (left-aligned).
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
# Creates two vertical pillars, side by side.
for i in range(thickness + 1):
    # Each pillar is made of 'H' repeated thickness times.
    # Center-align the first pillar within twice the thickness width and the second pillar within six times the thickness width.
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
# Creates a wide horizontal belt in the middle.
for i in range((thickness + 1) // 2):
    # The belt is made by repeating 'H' 5 times the thickness and center-aligning it within six times the thickness width.
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
# Creates two vertical pillars, side by side, similar to the top pillars.
for i in range(thickness + 1):
    # Each pillar is made of 'H' repeated thickness times.
    # Center-align the first pillar within twice the thickness width and the second pillar within six times the thickness width.
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
# Creates the inverted cone at the bottom of the design.
for i in range(thickness):
    # The left part of the cone (right-aligned) + center 'H' + right part of the cone (left-aligned).
    # The entire line is then right-aligned within six times the thickness width.
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
