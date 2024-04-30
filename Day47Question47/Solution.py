class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, res, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums, path, res, used)
                used[i] = False
                path.pop()
        
        nums.sort()  # Sort the input list to handle duplicates
        res = []
        used = [False] * len(nums)
        backtrack(nums, [], res, used)
        return res
