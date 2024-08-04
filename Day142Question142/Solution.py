# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return None
        
        # Initialize two pointers
        slow = head
        fast = head
        
        # Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next    # Move fast pointer by 2 steps
            
            if slow == fast:          # Cycle detected
                # Find the start of the cycle
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        
        # No cycle detected
        return None
