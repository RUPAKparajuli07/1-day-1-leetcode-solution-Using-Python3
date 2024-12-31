class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the string in-place.
        :param s: List[str] - input array of characters
        :return: None
        """
        # Two-pointer approach
        left, right = 0, len(s) - 1

        while left < right:
            # Swap characters at left and right indices
            s[left], s[right] = s[right], s[left]
            # Move the pointers closer
            left += 1
            right -= 1
