class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_element

    def next(self):
        """
        :rtype: int
        """
        current = self.next_element
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_element is not None
