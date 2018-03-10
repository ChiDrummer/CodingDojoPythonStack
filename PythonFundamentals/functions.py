"""Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number."""
#def odd_evens(start,stop):
 #   for num in range(start, stop):
  #      if num % 2 != 0:
   #         print "Number is {}. This an odd number".format(num)
    #    else:
     #       print "Number is {}. This is an even number".format(num)
#odd_evens(1, 20) 

"""Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.   """   

def multiply(lst, num):

    for index in range(0, len(lst)):
        lst[index] *= num
    return lst

#multiply([2,4,6,8,10], 5)
"""Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list."""
#output = [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
def layered_multiples(lst):
   
    new_array = []
    for x in lst:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x