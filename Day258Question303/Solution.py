from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Compute prefix sums
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate sum using prefix sums
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Example Usage:
# obj = NumArray([-2, 0, 3, -5, 2, -1])
# print(obj.sumRange(0, 2))  # Output: 1
# print(obj.sumRange(2, 5))  # Output: -1
# print(obj.sumRange(0, 5))  # Output: -3
