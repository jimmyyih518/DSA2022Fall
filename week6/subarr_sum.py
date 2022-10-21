"""
Subarray Sum
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

def subarray_sum(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = 1
    curr_sum = arr[0]
    while right <= len(arr):
        if curr_sum + arr[right] == target:
            return [left, right]
        elif curr_sum + arr[right] < target:
            right += 1
        
    return []
    
    
arr = [1, -20, -3, 30, 5, 4]
target = 7
print(subarray_sum(arr, target))