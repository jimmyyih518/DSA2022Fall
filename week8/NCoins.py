'''
How does one make change for N cents using the minimum amount of coins?
Example: N = 29, coins = [1,5,10,25]
25, 1, 1, 1, 1
Example: N = 29, coins = [0,1,5,10,12,25]
12,12,5
'''

def MinCoinChange(coins, change_amount):

    #Create the 1D dp table and traceback table
    #Since our "base case" is 0 change, we need to add one extra element
    #aka the "optimal minimum change" for 0 dollars is 0 coins
    coins = [0] + coins
    min_coins = [0]*(change_amount+1)
    coin_traceback = [0]*(change_amount+1)
    
    #solve our base case, not needed in our case but putting it here for the template
    min_coins[0] = 0
    
    #first we fill our table with null values
    for amount in range(1, change_amount+1):
        min_coins[amount] = float('inf')
    
    #calculate the minimum coins for each 
    #value from 1 to our desired total change_amount
    for amount in range(1, change_amount+1):
        for selected_coin in coins:
            if selected_coin <= amount:
                #this is where we "find" the previous optimal solution
                curr_min = min_coins[amount - selected_coin]
                if (
                    curr_min != float('inf') and 
                    curr_min + 1 < min_coins[amount]
                    ):
                    #if we find a better solution, we choose it
                    #also, we record the optimal coin selected in the traceback table
                    min_coins[amount] = curr_min + 1
                    coin_traceback[amount] = selected_coin
    
    #now we use our traceback table to rebuild the result
    #and get the combination of coins used to construct the optimal in min_coins table
    remaining_amount = change_amount
    coin_change_output = []
    
    #the traceback table tells us what the
    #"last most optimal coin used" is for our current change total amount
    #we continue to step through until we find all coins used
    while(remaining_amount>0):
        optimal_current_coin = coin_traceback[remaining_amount]
        coin_change_output.append(optimal_current_coin)
        remaining_amount = remaining_amount-optimal_current_coin
                    
    return {'minimum coins required': min_coins[change_amount], 
            'minimum coins combination': coin_change_output}


#Testing code
coins = [1, 5, 10, 12, 25]
print(MinCoinChange(coins, 18))
