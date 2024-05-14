class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Find the actual rotation amount
        k %= length
        
        if k == 0:
            return head
        
        # Traverse to find the new tail and the node just before it
        prev_tail = head
        for _ in range(length - k - 1):
            prev_tail = prev_tail.next
        
        # Update pointers to perform rotation
        new_head = prev_tail.next
        prev_tail.next = None
        tail.next = head
        
        return new_head
