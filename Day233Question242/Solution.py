class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count characters in both strings
        count_s, count_t = {}, {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        # Compare character counts
        return count_s == count_t
