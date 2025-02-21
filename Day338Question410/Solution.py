from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(mid):
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid  # Try for a smaller maximum sum
            else:
                left = mid + 1  # Increase mid if current division is invalid
                
        return left  # The minimum largest sum
