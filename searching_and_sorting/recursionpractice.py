"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # base cases based on value of positio
    if position == 0 or position == 1:
       return position

    # make recursive call here 
    first_num = 1 # will count for the previous number in the sequence
    second_num = 2 # will count for the previous previous number in the sequence

    return get_fib(position - first_num) + get_fib(position - second_num)


    # gets all numbers in list, but not needed here
    # if position == 1:
    #     return [0]  # return 0
    # elif position == 2:  # else if position is equal to 1
    #     return [1]
   
    # fib_list = get_fib(position - 1)
    # fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
    
    # return fib_list

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
