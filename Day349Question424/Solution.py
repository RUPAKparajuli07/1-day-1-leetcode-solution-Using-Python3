class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store character frequency
        max_freq = 0  # Max frequency of a single character in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Result variable to store the max length
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # Window size is (right - left + 1), non-max_freq chars must be <= k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1  # Shrink the window from the left
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
