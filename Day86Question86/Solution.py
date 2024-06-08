# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Connect the less list to the greater list
        less.next = greater_head.next
        # Ensure the last node of the greater list points to None
        greater.next = None
        
        # The head of the new list is the next of less_head dummy
        return less_head.next
