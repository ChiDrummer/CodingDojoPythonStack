"""STRING AND LIST PRACTICE: Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:"""

"""string = "ABCDEFGHIJKL ABCDEFGHIJK"

list = [0,1,2,3,4,5,6,7,8,9]

string.find("B") #find the first iteration of B -> 1

string.find("J", 10) #find J starting at position 10 -> 22

string.find("A", 3, 23)#find "A" starting at 3 and ending at 23 -> 13

string = "Hello World!"

string.replace("World", "Eric")#replaces world with Eric

min(list)#returns 0

max(list)#returns 9

list = [2,5,7,3,1,9,6,8,0]

list.sort()#returns [0,1,2,3,4,5,6,7,8,9]

list.sort(reverse=True)#returns list in decending order [9,8,7,6...]

len(list)#would return number of items in a list

len(string)#"hello World!" = 12

words = "It's thanksgiving day. It's my birthday,too!"

words.replace("day", "mouth")#replace "day" with "mouth""""

"""Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list."""
"""x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[7]#prints Hello World
y = []
y.append(x.pop(0))
y.append(x.pop(7))
print y"""

"""Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]"""

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
x2 = x.pop(x[0:5])
x.insert(0, x2)