# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the linked list has less than two nodes, no swapping needed
        if not head or not head.next:
            return head
        
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Moving pointers forward for the next iteration
            prev = first_node
            head = first_node.next
        
        return dummy.next
