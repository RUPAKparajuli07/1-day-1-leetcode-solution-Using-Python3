class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the cache capacity
        self.capacity = capacity
        # Initialize the cache (hash map) and linked list (dummy nodes)
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        # Remove node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        # Add node right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # Get the value from the cache if it exists
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Check if the key is already in the cache
        if key in self.cache:
            # Update the value
            node = self.cache[key]
            node.value = value
            # Move the node to the front
            self._remove(node)
            self._add(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            # Add the new node to the cache
            self._add(new_node)
            self.cache[key] = new_node
            # Check if we need to evict an old node
            if len(self.cache) > self.capacity:
                # Remove the LRU node
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
