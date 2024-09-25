class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Shift both numbers to the right until they are the same
        shift = 0
        while left != right:
            left >>= 1  # Right shift left by 1
            right >>= 1  # Right shift right by 1
            shift += 1   # Count the number of shifts

        # Shift the common prefix back to its original place
        return left << shift  # Left shift the result by the number of shifts
