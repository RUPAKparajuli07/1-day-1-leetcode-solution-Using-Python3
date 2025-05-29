class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If strings are the same, no uncommon subsequence
        if a == b:
            return -1
        # If different, the longer string itself is the answer
        return max(len(a), len(b))
