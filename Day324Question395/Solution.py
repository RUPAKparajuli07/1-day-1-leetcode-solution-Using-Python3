class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0  # If the string is too short, return 0
        
        # Frequency count of characters in the string
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find a character that appears less than k times to use as a split point
        for char in char_count:
            if char_count[char] < k:
                # Split the string on this character and apply recursion
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # If every character appears at least k times, return the length of the string
        return len(s)

# Example test cases
solution = Solution()
print(solution.longestSubstring("aaabb", 3))   # Output: 3
print(solution.longestSubstring("ababbc", 2))  # Output: 5
