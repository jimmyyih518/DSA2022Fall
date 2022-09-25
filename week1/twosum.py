def twosum(nums, target):
    for n in nums:
        for m in nums:
            if n != m and n + m == target:
                return True
	
    return False
    
print(twosum(nums=[2,7,11,15], target=9))