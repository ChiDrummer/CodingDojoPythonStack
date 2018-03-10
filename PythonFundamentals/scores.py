"""Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A"""

import random
def grades(student):
    for x in range(0, student):
        score = random.randint(60,101)
        if score >= 60 and score <= 69:
            print "Score: {}; Your Grade is D".format(score)
        elif score >= 70 and score <= 79:
            print "Score: {}; Your Grade is C".format(score)
        elif score >= 80 and score <= 89:
            print "Score: {}; Your Grade is B".format(score)
        elif score >= 90 and score <= 100:
            print "Score: {}; Your Grade is A".format(score)
    print "End of Program!"
grades(10)