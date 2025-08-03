class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n  # Keep track of visited indices
        max_len = 0

        for i in range(n):
            if not visited[i]:
                start = i
                count = 0
                while not visited[start]:
                    visited[start] = True  # Mark as visited
                    start = nums[start]    # Move to next index
                    count += 1
                max_len = max(max_len, count)

        return max_len
