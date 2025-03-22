from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark visited indices
        for num in nums:
            index = abs(num) - 1  # Convert value to index
            nums[index] = -abs(nums[index])  # Mark index as visited (negative)

        # Step 2: Collect missing numbers
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

# Example usage:
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
print(sol.findDisappearedNumbers([1,1]))  # Output: [2]
