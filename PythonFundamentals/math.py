"""Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000."""

for number in range(1,101,2):
    print number

for number in range(5,100):
    if number % 5 == 0:
        print number

#sum the list
"""a = [1, 2, 5, 10, 255, 3]
print sum(a)"""

#average of list
"""a = [1, 2, 5, 10, 255, 3]
average = sum(a)/len(a)
print average"""

