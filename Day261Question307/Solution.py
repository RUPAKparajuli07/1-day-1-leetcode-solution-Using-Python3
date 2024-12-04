from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)  # Allocate space for the segment tree
        self.buildTree(nums, 0, 0, n - 1)  # Build the tree

    def buildTree(self, nums: List[int], node: int, start: int, end: int):
        if start == end:  # Leaf node
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.buildTree(nums, left_child, start, mid)
            self.buildTree(nums, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # Sum of children

    def update(self, index: int, val: int) -> None:
        self.updateTree(0, 0, self.n - 1, index, val)

    def updateTree(self, node: int, start: int, end: int, index: int, val: int):
        if start == end:  # Leaf node
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if index <= mid:  # Update the left subtree
                self.updateTree(left_child, start, mid, index, val)
            else:  # Update the right subtree
                self.updateTree(right_child, mid + 1, end, index, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # Update current node

    def sumRange(self, left: int, right: int) -> int:
        return self.queryTree(0, 0, self.n - 1, left, right)

    def queryTree(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or left > end:  # No overlap
            return 0
        if left <= start and end <= right:  # Complete overlap
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.queryTree(left_child, start, mid, left, right)
        right_sum = self.queryTree(right_child, mid + 1, end, left, right)
        return left_sum + right_sum

# Example Usage
# Initialize the NumArray object
numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))  # Output: 9
numArray.update(1, 2)           # Update index 1 to value 2
print(numArray.sumRange(0, 2))  # Output: 8
