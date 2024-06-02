from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        
        return i

# Example usage:
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = solution.removeDuplicates(nums)
print(k, nums[:k])  # Output: 5, nums = [1, 1, 2, 2, 3]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k = solution.removeDuplicates(nums)
print(k, nums[:k])  # Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
