class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0 and (n & (n - 1)) is 0
        return n > 0 and (n & (n - 1)) == 0
