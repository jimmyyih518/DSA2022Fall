#Get the nth fibonacci number
#Compare recursive and stack implementations

#Recursive Implementation example

def fibonacci_recursive(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_stack(n):
    if n in [0,1]: # bug fix, check base case first
        return n
        
    total = 0
    stack = [max(0,n-1)] # bug fix, add n-1 instead of n to stack
    while stack:
        curr = stack.pop()
        if curr in [0,1]: #base case 0 or 1 are first two in fibonacci sequence
            total += 1
        else:
            stack.append(curr - 1)
            stack.append(curr - 2)

    return total


    
#Testing Code
for i in range(10):
    print('n= ', i)
    print(fibonacci_recursive(i))
    print(fibonacci_stack(i))