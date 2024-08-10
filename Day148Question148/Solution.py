class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If the list has 0 or 1 elements, it's already sorted
        if not head or not head.next:
            return head

        # Find the midpoint of the list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        mid = slow.next
        slow.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        # Append any remaining nodes from either half
        curr.next = left or right

        return dummy.next
