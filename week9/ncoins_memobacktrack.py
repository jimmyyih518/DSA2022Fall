#NCoins problems solved using backtracking and memoization

# Backtracking part
def min_coins(coins, amount, sum, memo):
    # our "sum" will start at zero when it's first called
    # start by listing out our end conditions
    
    # we've found one possible solution
    if sum == amount:
        return 0

    # not a valid solution
    if sum > amount:
        return float('inf')

    # memoization: this solution has been found before, don't calculate just reuse
    if memo[sum] != -1:
        return memo[sum]

    # we're looking for a minimum, therefore initialize answer at a max value
    ans = float('inf')

    # iterate through all coins, much like DP
    for coin in coins:
        # recursively explore one path until we hit the end
        result = min_coins(coins, amount, sum + coin, memo)
        if result == float('inf'):
            continue
        # if we actually have a solution, that forms our new current best answer
        ans = min(ans, result + 1)

    # memoization: record this solution so we can reuse it
    memo[sum] = ans
    return ans

# Solving the problem
def coin_change(coins, amount):
    # our memoization table looks a lot like DP
    memo = [-1] * (amount + 1)
    
    # find the optimal result
    result = min_coins(coins, amount, 0, memo)
    
    # if optimal result exists return it, otherwise return -1
    if result != float('inf'):
        return result
    else:
        return -1
        
        
#Testing Code
coins = [1, 5, 2]
target = 11
print(coin_change(coins, target)) #expect 3, that's 5+5+1

coins = [1,5,10,12,25]
target = 29
print(coin_change(coins, target)) #expect 3, that's 12+12+5
