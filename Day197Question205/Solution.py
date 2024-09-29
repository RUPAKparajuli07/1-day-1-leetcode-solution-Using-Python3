class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionary to store mappings from s to t
        s_to_t = {}
        # Dictionary to store reverse mappings from t to s
        t_to_s = {}
        
        # Loop through both strings character by character
        for ch_s, ch_t in zip(s, t):
            # Check if there's a mapping from s to t
            if ch_s in s_to_t:
                # If mapped, check if it matches the current character in t
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                # If not mapped, create a new mapping
                s_to_t[ch_s] = ch_t
            
            # Check if there's a reverse mapping from t to s
            if ch_t in t_to_s:
                # If mapped, check if it matches the current character in s
                if t_to_s[ch_t] != ch_s:
                    return False
            else:
                # If not mapped, create a new reverse mapping
                t_to_s[ch_t] = ch_s
        
        # If no conflicts, return True
        return True
