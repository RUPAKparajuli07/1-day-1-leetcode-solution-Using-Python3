# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # Single node or empty list is a palindrome
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Check palindrome by comparing the two halves
        left, right = head, prev  # prev now points to the head of the reversed second half
        while right:  # Only need to compare till the end of the shorter half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # Step 4 (Optional): Restore the list to its original state by reversing the second half again
        # prev = None
        # while right:
        #     next_node = right.next
        #     right.next = prev
        #     prev = right
        #     right = next_node

        return True
