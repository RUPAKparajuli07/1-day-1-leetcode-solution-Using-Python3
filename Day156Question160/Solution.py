class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers
        pA, pB = headA, headB
        
        # Traverse both lists
        while pA != pB:
            # Move pointer A to the next node, or reset to headB if it reaches the end
            pA = pA.next if pA else headB
            
            # Move pointer B to the next node, or reset to headA if it reaches the end
            pB = pB.next if pB else headA
        
        # Return the intersection node or None
        return pA
