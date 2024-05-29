from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to count all characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Left and Right pointers
        left, right = 0, 0
        
        # Dictionary to keep track of the window's characters count
        window_counts = defaultdict(int)
        
        # Formed is the number of unique characters in the current window which match the required count in t
        formed = 0
        
        # Result tuple to store the length of the window, left and right pointers
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add one character from the right to the window
            character = s[right]
            window_counts[character] += 1
            
            # If the character is part of t and its count in the window matches its count in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'
            while left <= right and formed == required:
                character = s[left]
                
                # Save the smallest window until now
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead
                left += 1
            
            # Keep expanding the window
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
