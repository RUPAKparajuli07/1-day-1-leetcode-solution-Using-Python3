class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers for s and t
        i, j = 0, 0

        # Traverse through t while checking characters from s
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move to the next character in s
                i += 1
            j += 1  # Always move in t

        # If we have traversed all characters in s, then it's a subsequence
        return i == len(s)
