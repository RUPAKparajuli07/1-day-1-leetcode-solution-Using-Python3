# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Step 2: Traverse through the linked list
        while current.next is not None:
            if current.next.val == val:  # Step 3: If node's value equals the target value, skip it
                current.next = current.next.next
            else:
                current = current.next  # Move to the next node
        
        # Step 4: Return the new head (which is the next node of the dummy)
        return dummy.next
