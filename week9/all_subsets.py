'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Input: nums = [1,2,3]
Output: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]

'''

def subsets(nums):
    # draw the state space tree
    # what's our starting choice
    # what defines a possible end result
    
    # How do we start with a recursive function to solve this brute force?
    # Once the recursive method is done, think about ways to optimize
    
    # Remember we use depth first search (recursive) with backtracking
    def dfs():
        # what's our return condition?
        if condition:
            # do something
            return

        dfs() # continue to recursively explore current path

    # don't forget to actually call the dfs function
    dfs()

    return 
