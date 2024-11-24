class Solution:
    def canWinNim(self, n: int) -> bool:
        # You can win if n is not a multiple of 4
        return n % 4 != 0
