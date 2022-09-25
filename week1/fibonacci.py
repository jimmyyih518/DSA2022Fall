def fibonacci(n):
    
    fib_series = [0,1]
    if n <= 2:
        return fib_series[:n]
    else:
        curr_i = 2
        while curr_i < n:
            curr_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(curr_fib)
            curr_i += 1
        
        return fib_series
	
print(fibonacci(10))
print(fibonacci(7))
print(fibonacci(2))

#n = 3, fib_series = [0,1], next value is 0+1=1, append [1], fib_series = [0,1,1]
#n = 4, fib_seires = [0,1,1], next value is 1+1=2, append [2], fib_series = [0,1,1,2]


'''
def fibonacci_recursion(n):

    def get_fibonacci(n):
        if n <= 1:
            return n
        else:
            return get_fibonacci(n-1) + get_fibonacci(n-2)
                
    fib_series = []
    
    for i in range(n):
        fib_series.append(get_fibonacci(i))
        
    return fib_series
    
print(fibonacci_recursion(10))
'''