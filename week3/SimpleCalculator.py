#Implement a simple calculator

def math_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b

def calculator(arr):
    
    stack = []
    stack.append(arr[0])
    i = 1 # Starting at index 1 instead of 0
    while i < len(arr):
        if arr[i] in ('+','-','*','/'):
            a = stack.pop()
            b = stack.pop()
            result = math_operation(b, a, arr[i]) # Notice here, why did we flip a and b?
            stack.append(result)
        else:
            stack.append(arr[i])
        i += 1
    
    return stack[0]
    
#Testing Code

arr = [3, 3, '+', 2, '-', 2, '*']
print(calculator(arr))