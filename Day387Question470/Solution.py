# The rand7() API is already defined for you.
# def rand7():
#     return random.randint(1, 7)  # Returns 1 to 7 uniformly

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number from 1 to 49 (7 * 7)
            row = rand7()
            col = rand7()
            index = (row - 1) * 7 + col  # index is in range 1 to 49

            if index <= 40:
                return (index - 1) % 10 + 1  # map 1–40 to 1–10 uniformly
