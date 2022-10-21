"""
Given an array of integers sorted in ascending order, 
find two numbers that add up to a given target. 
Return the indices of the two numbers in ascending order. 
You can assume elements in the array are unique and 
there is only one solution. Do this in O(n) time and with constant auxiliary space.

Input: [2 3 4 5 8 11 18], 8

Output: 1 3
"""

def two_sum_sorted(arr, target):

    left = 0
    right = len(arr)-1
    
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        if arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    
    return
