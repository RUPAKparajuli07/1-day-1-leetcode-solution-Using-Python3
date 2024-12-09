class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Function to use BIT for range sum query and updates
        def update(bit, idx, delta):
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & -idx
        
        def query(bit, idx):
            sum_ = 0
            while idx > 0:
                sum_ += bit[idx]
                idx -= idx & -idx
            return sum_
        
        # Step 1: Coordinate compression to handle the range of numbers in nums
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}  # 1-based indexing
        
        # Step 2: Initialize BIT (Fenwick Tree)
        n = len(nums)
        bit = [0] * (n + 1)  # Fenwick Tree with size n+1 (1-based indexing)
        result = []
        
        # Step 3: Traverse the numbers in reverse order (right to left)
        for num in reversed(nums):
            # Step 4: Query the BIT to find the number of smaller elements
            rank_num = rank[num]  # Get the compressed rank of the number
            result.append(query(bit, rank_num - 1))  # Query how many smaller elements are before
            update(bit, rank_num, 1)  # Update the BIT to reflect the current number
        
        # Step 5: Reverse the result to get the counts in the original order
        return result[::-1]
