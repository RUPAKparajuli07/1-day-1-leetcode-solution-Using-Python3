from sortedcontainers import SortedList

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        # Iterate over all pairs of row indices
        for top in range(m):
            # Initialize a 1D array to store column sums
            col_sums = [0] * n
            for bottom in range(top, m):
                # Update column sums
                for col in range(n):
                    col_sums[col] += matrix[bottom][col]
                
                # Use a sorted list to find the maximum subarray sum <= k
                sorted_prefix_sums = SortedList([0])
                cur_sum = 0
                for sum_val in col_sums:
                    cur_sum += sum_val
                    # Find the smallest prefix sum such that cur_sum - prefix_sum <= k
                    target = cur_sum - k
                    idx = sorted_prefix_sums.bisect_left(target)
                    if idx < len(sorted_prefix_sums):
                        max_sum = max(max_sum, cur_sum - sorted_prefix_sums[idx])
                    sorted_prefix_sums.add(cur_sum)
        
        return max_sum
