class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_sublist(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Check if there are k nodes remaining
            end = prev_group_end
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            
            start_next = prev_group_end.next
            end_next = end.next
            # Reverse the current group
            prev_group_end.next = reverse_sublist(start_next, end_next)
            # Connect the reversed group
            start_next.next = end_next
            # Move pointers for the next group
            prev_group_end = start_next
        
        return dummy.next
