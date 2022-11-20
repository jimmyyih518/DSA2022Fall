'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Input: nums = [1,2,3]
Output: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]

'''

def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    res = []
    def dfs(i, cur):
        if i == n:
            res.append(cur)
            return

        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)

    dfs(0, [])

    return res
