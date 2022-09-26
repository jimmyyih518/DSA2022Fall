#Get the nth fibonacci number
#Implement using a stack data structure

#Recursive Implementation example
'''
def get_fibonacci(n):
    if n <= 1:
        return n
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)
'''

def fibonacci(n):
    total = 0
    stack = [n]
    while len(stack) > 0:
        curr = stack.pop()
        if curr in [0,1]:
            total += 1
        else:
            stack.append(curr - 1)
            stack.append(curr - 2)

    return total
    
#Testing Code
for i in range(10):
    print(fibonacci(i))