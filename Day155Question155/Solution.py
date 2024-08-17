class MinStack:

    def __init__(self):
        # Initialize two stacks: one for the values and one for the minimum values
        self.stack = []  # main stack to store all the values
        self.min_stack = []  # stack to store the minimum values

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the minimum value onto the min_stack
        # If min_stack is empty or val is smaller or equal to the top of min_stack, push val
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        popped_value = self.stack.pop()
        # If the popped value is the same as the top of the min_stack, pop the min_stack too
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top value from the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top value from the min_stack, which is the minimum value in the main stack
        return self.min_stack[-1]

# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())    # Output: 0
print(minStack.getMin()) # Output: -2
