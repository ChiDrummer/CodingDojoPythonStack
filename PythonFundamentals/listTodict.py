"""Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length."""

def make_dict(list1, list2):
    new_dict = dict(zip(list1, list2))
    print new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
make_dict(name, favorite_animal)