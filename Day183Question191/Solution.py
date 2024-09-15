class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize count of set bits (1s)
        
        # Iterate until n becomes 0
        while n:
            count += n & 1  # Add 1 to count if the last bit is 1
            n >>= 1  # Right shift n by 1 bit
        
        return count  # Return the total count of 1s
