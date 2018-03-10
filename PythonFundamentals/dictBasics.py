"""Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language."""

def makeDict(keys, values):
    dictionary = dict(zip(key_list, val_list))
    print dictionary
    
    for k,v in dictionary.items():
        print "My {} is {}.".format(k,v)

key_list = ["Name", "Age", "Country of Birth", "Favorite Language"]
val_list = ["Eric", "40","USA", "Python"]
makeDict(key_list, val_list)