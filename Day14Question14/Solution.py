from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Iterate through characters of the first string
        for i, char in enumerate(strs[0]):
            # Check if character matches in all other strings
            for s in strs[1:]:
                # If index out of range or character mismatch, return prefix found so far
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        # If all strings are identical, return the first string
        return strs[0]

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))      # Output: ""
