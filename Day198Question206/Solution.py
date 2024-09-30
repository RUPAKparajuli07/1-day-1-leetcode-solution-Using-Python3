# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None or only one node, return head
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list recursively
        new_head = self.reverseList(head.next)
        
        # Adjust the current node's next node to point to itself
        head.next.next = head
        head.next = None  # Set the current node's next to None
        
        return new_head  # Return the new head of the reversed list
