class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the index of the last occurrence of each character
        char_index = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            # If the current character is already in the dictionary and its index is after the start of the current substring,
            # update the start pointer to the index after the last occurrence of this character
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            # Update the index of the current character
            char_index[s[end]] = end

            # Update the maximum length if needed
            max_length = max(max_length, end - start + 1)

        return max_length
