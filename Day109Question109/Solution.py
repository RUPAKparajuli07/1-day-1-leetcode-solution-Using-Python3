class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMiddle(self, head):
        """
        This function will find the middle node of the linked list.
        """
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr is not None and fast_ptr.next is not None:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # Handling the case when slow_ptr was the head
        if prev_ptr is not None:
            prev_ptr.next = None
        
        return slow_ptr

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        This function will convert the sorted linked list to a height-balanced BST.
        """
        # Base case
        if not head:
            return None

        # Find the middle element of the linked list
        mid = self.findMiddle(head)
        
        # The middle element becomes the root
        node = TreeNode(mid.val)
        
        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
