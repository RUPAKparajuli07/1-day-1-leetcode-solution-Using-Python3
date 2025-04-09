class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Stores max length of valid substring ending with each character
        max_len_end_with = [0] * 26
        
        # Current length of valid substring
        curr_len = 0
        
        for i in range(len(s)):
            # Check if s[i] follows s[i-1] in wraparound order
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                curr_len += 1
            else:
                curr_len = 1  # Reset current length
            
            index = ord(s[i]) - ord('a')
            max_len_end_with[index] = max(max_len_end_with[index], curr_len)
        
        # Sum of all maximum lengths gives the total unique substrings
        return sum(max_len_end_with)
