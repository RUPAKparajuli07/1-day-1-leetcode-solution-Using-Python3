from collections import deque

class MyStack:

    def __init__(self):
        # Initialize two queues
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Push to queue2
        self.queue2.append(x)
        
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the queues so that queue1 has the new order
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        # Pop from the front of queue1 (the top of the stack)
        return self.queue1.popleft()

    def top(self) -> int:
        # Peek at the front of queue1 (the top of the stack)
        return self.queue1[0]

    def empty(self) -> bool:
        # Check if queue1 is empty
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
