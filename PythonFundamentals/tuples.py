"""Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:"""

def make_tuple(dictionary):
    print list(dictionary.items())

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
make_tuple(my_dict)