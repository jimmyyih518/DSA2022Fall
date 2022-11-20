'''
Knapsack problem
Given weights and values of n items, put these items into a knapsack of capacity W
You want to maximize the total value of the knapsack
You cannot break an item, either pick it or don’t pick it (the 0-1 property)

Example:
value = [60, 100, 120], weight = [10, 15, 20], capacity = 40
Answer = 220
Explanation:
You can put the second and third items in the knapsack, 
with a combined weight of 15+20 = 35 which is less than the total capacity W. 
This also maximizes the value of the items in the knapsack at 220.

'''

def max_value_knapsack(values, weights, max_capacity, print_table = False):
    # first we want to sort the items by weight
    # we also need to rearrange the values accordingly
    weights, values = sort_weight_values(weights, values)
    
    # total number of items, we can also find it from weights count
    num_items = len(values)
    
    # variables: what weight we put in, which items we put in
    # constraints: max_capacity
    # objective: value -> maximize
    
    # the dynamic programming table
    # this time it is 2D, we're looking at bag capacity and which items we're putting in
    # start the optimal (max) values at zero for all cases
    table = [[0 for _ in range(max_capacity+1)] for _ in range(num_items+1)]
    
    # we already know the base case is zero value if we put nothing in
    
    # now we start filling in the table for the rest of the columns/rows
    # start with each item (we're referencing item by index)
    for item in range(num_items+1):
        # can this item improve the current max value (default 0)
        for capacity in range(max_capacity+1):
            # simple base case to check zero capacity
            if item == 0 or capacity == 0:
                table[item][capacity] = 0
                
            # do we still have capacity in the bag left to put more items in?
            elif weights[item-1] <= capacity:
                # if we do, then see if adding this new item in improves our result at the current capacity
                curr_optimal = table[item-1][capacity]
                new_optimal = values[item-1] + table[item-1][capacity-weights[item-1]]
                table[item][capacity] = max(curr_optimal, new_optimal)
            # otherwise if we can't put more items in, then the previous value is still the best for the current capacity
            else:
                table[item][capacity] = table[item-1][capacity]

    if print_table:
        import pandas as pd
        df = pd.DataFrame(table).transpose()
        return df
    else:
        return table[num_items][max_capacity]


def sort_weight_values(weights, values):
    # helper function to sort by weights and rearrange values
    zipped_lists = zip(weights, values)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    
    sorted_weights, sorted_values = [ list(tuple) for tuple in tuples]
    return sorted_weights, sorted_values


#Testing Code
values = [60, 100, 120]
weights = [10, 15, 20]
max_capacity = 40

#print(max_value_knapsack(values, weights, max_capacity))

#print dp table code
print(max_value_knapsack(values, weights, max_capacity, True))
