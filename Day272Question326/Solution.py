class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Base case: return False if n is non-positive
        if n <= 0:
            return False
        
        # The maximum power of three that fits in a 32-bit integer
        max_power_of_three = 3 ** 19  # 3^19 = 1162261467 (highest power of 3 under 2^31)
        
        # Check if n divides the maximum power of three
        return max_power_of_three % n == 0
