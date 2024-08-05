class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the list to be in the form: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        """
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None  # Split the list into two halves
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev  # Now `second` is the head of the reversed second half
        
        # Step 3: Merge the two halves
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
