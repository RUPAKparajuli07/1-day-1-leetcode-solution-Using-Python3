class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count the frequency of each character
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        # Step 2: Find the first character with a frequency of 1
        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        
        # Step 3: If no unique character is found, return -1
        return -1
