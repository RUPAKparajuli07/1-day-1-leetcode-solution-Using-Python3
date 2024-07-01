# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def helper(left, right):
            if left > right:
                return None

            # Choose middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            
            return node

        return helper(0, len(nums) - 1)
