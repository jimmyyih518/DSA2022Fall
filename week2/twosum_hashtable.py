#Twosum revisited
#Solving using Hashtable approach

def twosum(nums, target):
    nums_set = set(nums)
    for n in nums:
        if target - n != n and target - n in nums_set:
            return True
    return False
    
print(twosum(nums=[2,7,11,15], target=9))
print(twosum(nums=[2,7,11,15], target=10))
