"""Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears."""
import random
#heads = 1
#tails = 0
def coinToss(tosses):
    print "Starting Program"

    count = 0
    sumHead = 0
    sumTail = 0

    for x in range(1,tosses + 1):
        result = random.randint(0,1)
        count = count + 1
        if result == 0:
            sumTail = sumTail + 1
            print "Attempt #{}: Its a TAIL..... Heads = {}  Tails = {}".format(count, sumHead, sumTail)

        else:
            sumHead = sumHead + 1
            print "Attempt #{}: Its a HEAD..... Heads = {}  Tails = {}".format(count, sumHead, sumTail)
    print "Program End"
coinToss(5)
