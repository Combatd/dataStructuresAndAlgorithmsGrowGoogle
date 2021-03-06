"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    midpoint = int(len(input_array) / 2) # midpoint will be lower number if len(input_array) is even
    savedLocation = 0 # the index will start at 0
    for index, number in enumerate(input_array, start=midpoint): # enumerate through the array starting at the midpoint
        if number == value:
            return savedLocation
            break
        
        savedLocation += 1 # iterate this before moving to next iteration

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))