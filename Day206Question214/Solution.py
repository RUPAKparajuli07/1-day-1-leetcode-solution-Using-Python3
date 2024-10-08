class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Step 1: Reverse the string
        rev_s = s[::-1]
        
        # Step 2: Combine original string and reversed string with a separator
        new_s = s + "#" + rev_s
        
        # Step 3: KMP failure function to find the longest palindromic prefix
        n = len(new_s)
        lps = [0] * n  # Longest prefix suffix array
        
        # Build the LPS array
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # Step 4: Use the LPS array to construct the shortest palindrome
        # The length of the longest palindromic prefix is given by lps[-1]
        add_length = len(s) - lps[-1]  # Characters to add from the reversed part
        return rev_s[:add_length] + s

# Example usage:
sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(sol.shortestPalindrome("abcd"))      # Output: "dcbabcd"
