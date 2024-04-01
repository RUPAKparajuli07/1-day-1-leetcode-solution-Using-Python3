from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to easily handle duplicates
        
        def kSum(nums: List[int], target: int, k: int, start: int) -> List[List[int]]:
            res = []
            if start == len(nums) or nums[start] * k > target or target > nums[-1] * k:
                return res
            
            if k == 2:
                return twoSum(nums, target, start)
            
            for i in range(start, len(nums)):
                if i == start or nums[i - 1] != nums[i]:
                    for _, subset in enumerate(kSum(nums, target - nums[i], k - 1, i + 1)):
                        res.append([nums[i]] + subset)
            return res
        
        def twoSum(nums: List[int], target: int, start: int) -> List[List[int]]:
            res = []
            lo, hi = start, len(nums) - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total < target or (lo > start and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif total > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        
        return kSum(nums, target, 4, 0)

# Example usage:
solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2,2,2,2,2], 8))      # Output: [[2,2,2,2]]
