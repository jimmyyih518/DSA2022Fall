#Find Kth largest elements repeated on array

import heapq

class MyArray:
	def __init__(self, nums):
		self.nums = nums
		heapq.heapify(self.nums)
        
	def FindKLargest(self, k):
		
		k_largest = heapq.nlargest(k, self.nums) # Modify this portion
		
		return k_largest[-1]
        
        
#Testing Code
arr = MyArray([3,2,1,5,6,4])
print(arr.FindKLargest(2))
print(arr.FindKLargest(1))
print(arr.FindKLargest(4))
print(arr.FindKLargest(3))

#...assume FindKLargest will be called many more times
