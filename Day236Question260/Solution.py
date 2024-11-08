from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get xor_all = a ^ b
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a set bit that is different between a and b
        # We use xor_all & -xor_all to get the rightmost set bit
        diff_bit = xor_all & -xor_all
        
        # Step 3: Divide numbers into two groups based on the diff_bit
        a, b = 0, 0
        for num in nums:
            if num & diff_bit:
                a ^= num  # XOR numbers in the first group
            else:
                b ^= num  # XOR numbers in the second group
        
        # Step 4: a and b are the two unique numbers
        return [a, b]
