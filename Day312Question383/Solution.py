class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count characters in magazine
        char_count = {}
        
        # Count the frequency of each character in magazine
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False  # Not enough characters in magazine
            char_count[char] -= 1  # Use one occurrence of the character
        
        return True  # All characters in ransomNote can be constructed
