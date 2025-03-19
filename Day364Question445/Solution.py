class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize prev as None and curr as the head of the list.
        prev = None
        curr = head

        # Traverse through the list and reverse the pointers.
        while curr:
            # Store the next node temporarily
            nxt = curr.next
            # Reverse the pointer of the current node
            curr.next = prev
            # Move prev and curr one step forward
            prev = curr
            curr = nxt
        
        # Return the new head of the reversed list
        return prev

    def helper(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to start building the result list
        dummyHead = ListNode(0)
        # Tail points to the current last node of the result list
        tail = dummyHead
        # Initialize carry (to handle values > 9)
        carry = 0

        # Process both linked lists until we finish both or there is no carry left
        while l1 or l2 or carry:
            # Get the current digit from l1 and l2, if present, otherwise 0
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Calculate the sum of current digits plus any carry
            total = digit1 + digit2 + carry
            # The new digit is the remainder of the total divided by 10
            digit = total % 10
            # Carry for the next iteration is the quotient of total divided by 10
            carry = total // 10

            # Create a new node with the calculated digit and append it to the result list
            newNode = ListNode(digit)
            tail.next = newNode
            # Move the tail pointer to the new node
            tail = tail.next

            # Move to the next node in l1 and l2 if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the actual result list starting from the node after dummyHead
        result = dummyHead.next
        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Step 1: Reverse both input linked lists so we can add from the least significant digit
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        # Step 2: Add the numbers digit by digit using helper function
        ans = self.helper(l1, l2)

        # Step 3: Reverse the result to restore the correct order (most significant digit first)
        return self.reverseList(ans)
