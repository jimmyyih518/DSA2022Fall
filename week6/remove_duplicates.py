"""
Given a sorted list of numbers, 
remove duplicates and return the new length. 
You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so the 
first 3 elements becomes 0, 1, 2. Return 3 because the new length is 3.
"""

def remove_duplicates(arr):

    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
            

    
    return slow + 1
    
#Testing Code
arr = [1,1,1,2,2,3,3,3]
print(remove_duplicates(arr))