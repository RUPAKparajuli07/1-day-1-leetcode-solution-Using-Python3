# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the merged list
        current = dummy  # Pointer to keep track of the current node in the merged list

        # Iterate through both lists until one of them becomes None
        while list1 is not None and list2 is not None:
            # Compare the values of the current nodes of list1 and list2
            if list1.val <= list2.val:
                current.next = list1  # Connect current node to list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                current.next = list2  # Connect current node to list2
                list2 = list2.next  # Move list2 pointer forward
            current = current.next  # Move the current pointer of the merged list forward

        # Connect the remaining nodes of the non-empty list to the merged list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return dummy.next  # Return the next node of dummy, which is the head of the merged list
