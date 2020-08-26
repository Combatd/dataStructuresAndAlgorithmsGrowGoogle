"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # base cases based on value of position
    # if position is equal to 1
    if position == 0:
        return [0]  # return 0
    elif position == 1: # else if position is equal to 1
        return [1]

    # make recursive call here 
    fib_list = get_fib(position - 1)
    fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
    
    return fib_list

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))