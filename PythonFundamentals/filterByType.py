"""Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

TEst with this:
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']"""


variable = ##

if type(variable) == int:
    if variable >= 100:
        print "Thats a big number"

    else:
        print "Thats a small number"


elif type(variable) == str:
    if len(variable) >= 50:
        print "Long sentence"

    else:
        print "Short sentence"

elif type(variable) == list:
    if len(variable) >= 10:
        print "big list"

    else:
        print "small List"

 