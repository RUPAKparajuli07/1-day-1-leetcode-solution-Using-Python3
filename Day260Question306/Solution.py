class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, remaining):
            # Continuously check if remaining numbers form a valid additive sequence
            while remaining:
                # Calculate the next number in the sequence
                sum_str = str(int(num1) + int(num2))
                # If the next part of the sequence doesn't match, it's invalid
                if not remaining.startswith(sum_str):
                    return False
                # Update numbers and remaining string
                num1, num2 = num2, sum_str
                remaining = remaining[len(sum_str):]
            return True
        
        n = len(num)
        # Try all combinations for the first two numbers
        for i in range(1, n):  # First number ends at i
            for j in range(i + 1, n):  # Second number ends at j
                num1 = num[:i]
                num2 = num[i:j]
                # Check for leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                # Validate if this split leads to a valid additive sequence
                if is_valid(num1, num2, num[j:]):
                    return True
        return False
