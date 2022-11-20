'''
Knapsack problem
Given weights and values of n items, put these items into a knapsack of capacity W
You want to maximize the total value of the knapsack
You cannot break an item, either pick it or don’t pick it (the 0-1 property)

Example:
value = [60, 100, 120], weight = [10, 15, 20], W = 40
Answer = 220
Explanation:
You can put the second and third items in the knapsack, 
with a combined weight of 15+20 = 35 which is less than the total capacity W. 
This also maximizes the value of the items in the knapsack at 220.

'''

def max_value_knapsack(value, weight, W):
    # what is our base case here?
    # what is the "sub problem" we're trying to solve?
    # what is a scenario for a potential "overlapping subproblem"
    
    # How do we setup the DP table
    # Do we need a traceback table in this particular problem?
    
    # solve the base case, for reference
    
    # fill the rest of the DP table with an appropriate null value
    
    # iterate through the DP table and calculate the optimal at each point
    # build our solution using previous calculated optimal values
    
	
	return


	
#Testing Code
value = [60, 100, 120]
weight = [10, 15, 20]
W = 40
print(max_value_knapsack(value, weight, W))