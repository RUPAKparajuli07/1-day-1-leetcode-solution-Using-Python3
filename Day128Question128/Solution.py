from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If nums is empty, return 0
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
