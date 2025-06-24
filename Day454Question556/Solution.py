class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))  # Step 1: Convert to list of characters
        i = len(digits) - 2

        # Step 2: Find the first digit that is smaller than its next digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # Step 3: If no such digit is found, return -1
        if i == -1:
            return -1

        # Step 4: Find the smallest digit on the right side of i that is bigger than digits[i]
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 5: Swap them
        digits[i], digits[j] = digits[j], digits[i]

        # Step 6: Reverse the subarray to the right of i
        digits[i + 1:] = reversed(digits[i + 1:])

        # Step 7: Convert back to integer
        result = int(''.join(digits))

        # Step 8: Check 32-bit constraint
        return result if result < (1 << 31) else -1
