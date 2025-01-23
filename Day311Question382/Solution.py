import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        """
        Initializes the object with the head of the singly-linked list.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Chooses a node randomly from the linked list and returns its value.
        Uses reservoir sampling to ensure equal probability.
        """
        result = -1  # This will store the selected random value
        current = self.head  # Start with the head of the list
        index = 0  # Position of the current node in the linked list
        
        while current:
            # Randomly replace the result with the current node's value
            if random.randint(0, index) == 0:  # Probability of 1/(index+1)
                result = current.val
            current = current.next
            index += 1  # Increment the index
        
        return result
