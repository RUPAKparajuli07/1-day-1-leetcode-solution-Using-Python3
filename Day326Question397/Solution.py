class Solution:
    def integerReplacement(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def helper(x):
            if x == 1:
                return 0  # Base case: 1 requires 0 operations
            if x % 2 == 0:
                return 1 + helper(x // 2)  # Even case: n / 2
            else:
                return 1 + min(helper(x + 1), helper(x - 1))  # Odd case: min(n+1, n-1)

        return helper(n)
