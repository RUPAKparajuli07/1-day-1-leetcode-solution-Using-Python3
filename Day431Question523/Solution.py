class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1}  # remainder: index
        total = 0

        for i, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder in mod_map:
                if i - mod_map[remainder] > 1:
                    return True
            else:
                mod_map[remainder] = i

        return False
