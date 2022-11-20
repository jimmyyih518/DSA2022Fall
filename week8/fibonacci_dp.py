'''
Revisit fibonacci sequence using DP

get the Nth fibonacci number in the sequence
using dynamic programming
'''

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

# Testing Code
for i in range(10):
    print(fibonacci_dp(i))