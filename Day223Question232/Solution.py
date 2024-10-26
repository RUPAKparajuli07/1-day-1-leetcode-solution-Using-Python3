class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack_in = []  # Stack for push operations
        self.stack_out = [] # Stack for pop/peek operations

    def push(self, x: int) -> None:
        # Push the element onto the input stack
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the elements in correct order
        self._transfer_in_to_out()
        # Pop the top element from stack_out
        return self.stack_out.pop()

    def peek(self) -> int:
        # Ensure stack_out has the elements in correct order
        self._transfer_in_to_out()
        # Peek at the top element of stack_out
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out

    def _transfer_in_to_out(self):
        # Helper function to transfer elements from stack_in to stack_out
        if not self.stack_out:  # Only transfer if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
