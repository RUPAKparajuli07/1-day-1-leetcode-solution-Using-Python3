from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)  # Count occurrences of each character
        length = 0
        odd_found = False

        for count in char_count.values():
            length += (count // 2) * 2  # Add pairs of characters
            if count % 2 == 1:  # Check if there's an odd count
                odd_found = True
        
        return length + 1 if odd_found else length  # Add 1 if any odd character exists
