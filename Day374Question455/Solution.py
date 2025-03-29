from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes
        
        i, j = 0, 0  # Two pointers
        content_children = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If the cookie satisfies the child's greed
                content_children += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie
        
        return content_children
