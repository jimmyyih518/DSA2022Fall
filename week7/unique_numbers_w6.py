'''
Unique numbers in array
Given a sorted array nums, find all unique elements in array.
The total number of elements in the array is much larger than the number of unique elements in the array.
Constraint: Must solve in less than O(n) time where n is number of elements in array
You may use any algorithm or data structure you’ve learnt so far
'''

def unique_in_arr(nums):
    # Initalize empty array to store output
    result = []

    # start pointer at index 0
    curr_idx = 0
    
    while curr_idx < len(nums):
        # Get current value and append to result
        curr_value = nums[curr_idx]
        result.append(curr_value)
        
        # Binary search to find the index of last occurence of an element in sorted array
        curr_last_idx = binary_search(nums, curr_value)

        # Move pointer up to the first occurence of next number
        curr_idx = curr_last_idx + 1
    
    return result
    
def binary_search(nums, target):
    
    left = 0
    right = len(nums) - 1
    idx = 0
    
    while left <= right:
        mid = (left + right) // 2
        # Condition that defines last occurence
        if (mid == len(nums) - 1 or nums[mid+1] > target) and nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return idx

#Testing Code

nums = [1,1,1,2,2,3,3,3]
#check that our binary search works
print(binary_search(nums, 1)) # expect output=2
print(binary_search(nums, 2)) # expect output=4


print(unique_in_arr(nums))