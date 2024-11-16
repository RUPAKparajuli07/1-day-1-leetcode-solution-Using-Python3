# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2  # Avoid overflow for large n
            if isBadVersion(mid):
                right = mid  # Narrow down to the left half
            else:
                left = mid + 1  # Narrow down to the right half
        return left  # left is the first bad version
