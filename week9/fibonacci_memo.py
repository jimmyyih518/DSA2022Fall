from time import time

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Memoization using a dictionary as our cache
def fibonacci_memo_dict(n, cache={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_memo_dict(n-1, cache) + fibonacci_memo_dict(n-2, cache)
        return cache[n] 
        

# Memoization using function-based decorators

def memoize(f):
    cache = {}
    def memoized_function(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return memoized_function


@memoize
def fibonacci_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)

# dynamic programming version here:

def fibonacci_dp(n):
    # cover our base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # one dimensional dp table
    dp_table = []
    for i in range(n+1):
        dp_table.append(-1)

    # put our base cases into the dp table to start
    dp_table[0] = 0
    dp_table[1] = 1

    # now we build the solution up from the base case
    for i in range(2, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    # return the nth element from our 1D dp table, which is the answer
    return dp_table[n]



def timed_run(fun, *args):
    time_start = time()
    output = fun(*args)
    time_end = time()
    print(fun.__name__, ' output ', output)
    print('total time: ' , time_end-time_start)
    
    
    
# Testing code

input_n = 35
timed_run(fibonacci_recursive, input_n)
timed_run(fibonacci_memo, input_n)
timed_run(fibonacci_memo_dict, input_n)
timed_run(fibonacci_dp, input_n)