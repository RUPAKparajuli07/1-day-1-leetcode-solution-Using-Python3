class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # We keep dividing n by powers of 5 and add to the count
        while n >= 5:
            n //= 5
            count += n
        return count
