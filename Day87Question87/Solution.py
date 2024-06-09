class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(i1, i2, length):
            # Base case: if the substrings are equal
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True
            # If the sorted substrings are not equal, they cannot be scrambles
            if sorted(s1[i1:i1+length]) != sorted(s2[i2:i2+length]):
                return False
            # Try to split the substring into two parts and check recursively
            for k in range(1, length):
                # Case 1: Without swapping
                if (dfs(i1, i2, k) and dfs(i1+k, i2+k, length-k)):
                    return True
                # Case 2: With swapping
                if (dfs(i1, i2+length-k, k) and dfs(i1+k, i2, length-k)):
                    return True
            return False
        
        return dfs(0, 0, len(s1))
