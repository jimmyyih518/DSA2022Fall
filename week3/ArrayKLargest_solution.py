#Find Kth largest elements repeated on array

import heapq

class MyArray:
    def __init__(self, nums):
        self.nums = [-1 * x for x in nums]
        heapq.heapify(self.nums)

    def FindKLargest(self, k):

        i = 0
        temp_values = []
        while i < k:
            popped_val = heapq.heappop(self.nums)
            temp_values.append(popped_val)
            i += 1

        while len(temp_values)>0:
            heapq.heappush(self.nums, temp_values.pop())

        return -1 * popped_val
        
        
#Testing Code
arr = MyArray([3,2,1,5,6,4])
print(arr.FindKLargest(2))
print(arr.FindKLargest(1))
print(arr.FindKLargest(4))
print(arr.FindKLargest(3))

#...assume FindKLargest will be called many more times, let's say M times
#Whats the time complexity of each step?




'''
#Another variation of the solution
class MyArray:
    def __init__(self, nums):
        self.nums = nums

    def FindKLargest(self, k):
        k_largest = heapq.nlargest(k, self.nums)
        
        return k_largest[-1]
        
    
'''