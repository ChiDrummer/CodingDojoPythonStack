"""Create a function called draw_stars() that takes a list of numbers and prints out * equal to the interger at that inex."""

def draw_stars(arr):
    for x in arr:
        print "*" * x
draw_stars([4, 6, 1, 3, 5, 7, 25])

"""Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part."""

def draw_stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            print x[0].lower() * len(x)
draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])





