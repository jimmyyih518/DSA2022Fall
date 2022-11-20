'''
Ncoins
How do you give change for N cents?
We’ll use the normal coin denominations of
1, 5, 10, 25
Select the “optimal” solution
For NCoins: the least number of coins
25, 1, 1, 1, 1
We’re going to demonstrate the greedy approach today
This is also typically how a human would do it
'''

def Ncoins(coins, amount):
    
    # First we sort the coins in reverse values
    # starting from the largest denomination
    coins.sort(reverse=True)
    
    # Initialize our "remainder" value
    remainder = amount
    result = []
    # And we just simply keep removing the largest possible denomination
    # Until we get to zero cents
    while remainder > 0:
        # Try every coin
        for coin in coins:
            if remainder >= coin:
                remainder -= coin
                result.append(coin)
                # As soon as one coin worked, we stop trying more coins in this iteration
                break
                
    return result
    
# Testing Code
coins = [1, 5, 10, 25]
amount = 29
print(Ncoins(coins, amount))

amount = 31
print(Ncoins(coins, amount))
