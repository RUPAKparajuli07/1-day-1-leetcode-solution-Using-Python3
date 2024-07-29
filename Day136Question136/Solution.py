from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num
        return single_num
