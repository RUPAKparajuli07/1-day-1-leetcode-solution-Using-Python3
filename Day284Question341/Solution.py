class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        Initialize the iterator with the nested list. 
        We use a stack to store the elements for efficient iteration.
        """
        self.stack = []
        self._flatten(nestedList)

    def _flatten(self, nestedList):
        """
        Helper function to flatten the nested list in reverse order 
        and push it onto the stack.
        """
        for element in reversed(nestedList):
            self.stack.append(element)

    def next(self) -> int:
        """
        Return the next integer in the flattened list.
        """
        if self.hasNext():
            return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        """
        Return True if there are still integers in the nested list.
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._flatten(top.getList())
        return False

# Example usage:
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
