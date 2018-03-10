"""Write a program that prints a 'checkerboard' pattern to the console.

Your program should require no input and produce console output that looks like so:
* * * *
 * * * *
* * * *
 * * * *
"""

l = [1,2,3,4,5,6,7,8]
red = "* * * *"
black = " * * * *"

for i in l:
    if i % 2 == 0:
        print red
    else:
        print black