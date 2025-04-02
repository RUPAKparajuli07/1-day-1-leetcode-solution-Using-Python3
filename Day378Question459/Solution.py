class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate string with itself
        doubled_s = s + s
        # Check if the original string appears in the doubled string
        # excluding the first and last character
        return s in doubled_s[1:-1]
