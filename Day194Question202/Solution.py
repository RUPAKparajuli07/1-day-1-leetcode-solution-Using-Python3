class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            # Function to calculate the sum of the squares of the digits
            total_sum = 0
            while number > 0:
                digit = number % 10  # Extract the last digit
                total_sum += digit ** 2  # Square the digit and add to total sum
                number //= 10  # Remove the last digit
            return total_sum

        seen_numbers = set()  # To track numbers we've seen
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)  # Add current number to the set
            n = get_next(n)  # Replace n with the sum of squares of digits

        return n == 1  # If we reach 1, the number is happy
