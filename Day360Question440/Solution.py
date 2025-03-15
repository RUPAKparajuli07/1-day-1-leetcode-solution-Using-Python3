class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_nodes(prefix, n):
            """ Count how many numbers exist with this prefix up to n """
            curr, next = prefix, prefix + 1
            count = 0
            while curr <= n:
                count += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return count
        
        curr = 1
        k -= 1  # As we start with '1' already counted

        while k > 0:
            count = count_nodes(curr, n)
            if k >= count:
                # Move to the next prefix
                k -= count
                curr += 1
            else:
                # Go deeper in the current prefix
                k -= 1
                curr *= 10
        
        return curr
