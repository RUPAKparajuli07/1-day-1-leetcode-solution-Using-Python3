from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Helper function to check if s is a subsequence of t
        def is_subsequence(s: str, t: str) -> bool:
            i = 0
            for char in t:
                if i < len(s) and s[i] == char:
                    i += 1
            return i == len(s)
        
        # Sort strings by length in descending order
        strs.sort(key=len, reverse=True)

        for i, s in enumerate(strs):
            if all(not is_subsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        
        return -1
