"""Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character."""

list1 = ["orange", "mango", "apple", "fig", "coconut"]
letter = "o"
newlist=[]

for x in list1:
    if (x.count(letter) != 0):
        newlist.append(x)

print newlist