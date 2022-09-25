#Bruteforce Sort Example
#example input nums = [1,5,2,4,3]
#example output [1,2,3,4,5]

def sort_array(nums):
    nums: list
    
    #nums.sort() #-> Default sort in python, we can use this to check our answer if needed
    
    for idx, val in enumerate(nums): #iteral through list
        min_val = min(nums[idx:]) #find minimum value
        min_val_loc = nums.index(min_val) #find location of this minimum value
        
        nums[min_val_loc], nums[idx] = nums[idx], nums[min_val_loc] #in place swap of the minimum value and current location value
    
    return
            

nums=[5,1,2,4,3]
sort_array(nums)    
print(nums)
