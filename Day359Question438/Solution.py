from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        # Frequency map of p
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])  # First window in s
        result = []

        # Compare first window
        if s_count == p_count:
            result.append(0)

        # Sliding window technique
        for i in range(len(p), len(s)):
            start_char = s[i - len(p)]
            new_char = s[i]

            # Remove the first character of the previous window
            s_count[start_char] -= 1
            if s_count[start_char] == 0:
                del s_count[start_char]  # Remove key if count is 0

            # Add the new character to the window
            s_count[new_char] += 1

            # Compare with p_count
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
