class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is greater than 0, is a power of 2, and the set bit is at an even position
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

# Examples
solution = Solution()
print(solution.isPowerOfFour(16))  # Output: True
print(solution.isPowerOfFour(5))   # Output: False
print(solution.isPowerOfFour(1))   # Output: True
