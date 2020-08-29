"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    midpoint = int(len(array) / 2)
    right_index = len(array)
    left_index = 0

    pivot = array[right_index - 1]
    before_pivot = array[right_index - 2]
    compared_number = array[left_index]

    if pivot < midpoint: return array

    print(midpoint, ' <- midpoint ', pivot, ' <- pivot', before_pivot, '<- before_pivot',  compared_number, ' <- compared_number')
    if pivot_lower_than_compared_number(pivot, compared_number):
        first_num = array.pop(left_index)
        array.append(first_num)  # moves first number to the end
        before_last_num = array.pop(right_index - 2) 
        array.insert(0, before_last_num) # moves second to last number to the front

    return array

# helper method
def pivot_lower_than_compared_number(pivot, compared_number):
    if pivot < compared_number: return True
    
    return False


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
