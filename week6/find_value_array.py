#Find value's index in array with binary search
#if the value doesn't exist, return -1

#Brute Force Example for reference

def find_value_bruteforce(nums, target):
    for idx, value in enumerate(nums):
        if value == target:
            return idx
            
    return -1
    
    
def find_value_binarysearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:  # <= because left and right could point to the same element, < would miss it
        mid = (left + right) // 2 # double slash for integer division in python 3, we don't have to worry about integer `left + right` overflow since python integers can be arbitrarily large
        # found target, return its index
        if nums[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if nums[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1 # if we get here we didn't hit above return so we didn't find target
    
    
#Testing Code
nums = [1,2,3,4,5,6]
target = 6

print(find_value_bruteforce(nums, target))
print(find_value_binarysearch(nums, target))