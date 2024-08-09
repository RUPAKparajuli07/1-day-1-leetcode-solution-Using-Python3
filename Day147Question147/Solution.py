# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the sorted list
        dummy = ListNode(float('-inf'))
        
        # Iterate through each node in the original list
        current = head
        while current:
            # At each iteration, remove the current node from the original list
            prev = dummy
            next_node = current.next  # Save the next node to process
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert the current node into the sorted part of the list
            current.next = prev.next
            prev.next = current
            
            # Move to the next node in the original list
            current = next_node
        
        # Return the sorted list starting after the dummy node
        return dummy.next
