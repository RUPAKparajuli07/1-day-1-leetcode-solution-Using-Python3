class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)  # XOR all characters
        return chr(result)  # Convert back to character
