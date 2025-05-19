class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # Initialize first two Fibonacci numbers
        a, b = 0, 1

        # Calculate up to nth number
        for i in range(2, n + 1):
            a, b = b, a + b

        return b
