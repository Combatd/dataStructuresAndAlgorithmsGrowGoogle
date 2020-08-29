"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# still needs to be solved properly
def quicksort(array):
    midpoint = int(len(array) / 2)

    pivot = array[midpoint]
    before_pivot = array[len(array) - 2]
    
    index = 0
    second_index = len(array) - 1
    compared_number = array[second_index]
    while index < len(array) - 1:
        if pivot_lower_than_compared_number(array[index], array[second_index]):
            first_num = array.pop(index + 1)
            array.append(first_num)  # moves first number to the end
            before_last_num = array.pop(second_index - 1) 
            array.insert(0, before_last_num) # moves second to last number to the front
        index += 1
        second_index -= 1

    return array

# helper method
def pivot_lower_than_compared_number(pivot, compared_number):
    if pivot < compared_number: return True
    
    return False


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
