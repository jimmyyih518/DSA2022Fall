#Unique numbers in array
#Divide and Conquer implementation

def unique_in_arr(nums):
    #define base cases, aka edge cases that we know to start
    if len(nums) <= 1:
        return nums
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            return [nums[0]]
        else:
            return nums
    
    #Divide
    mid = len(nums) // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    #Conquer
    left_result = unique_in_arr(left_arr)
    right_result = unique_in_arr(right_arr)
    
    #Combine
    #There's an edge case when combining
    if left_result[-1] == right_result[0]: 
        left_result.pop()  
        
    result = left_result + right_result
    
    return result
    
#Testing Code

nums = [1,1,1,2,2,3,3,3]
print(unique_in_arr(nums))