class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}  # Maps keys to their counts
        self.freq_map = {}  # Maps counts to their respective nodes
        self.head = Node(float('-inf'))  # Dummy head
        self.tail = Node(float('inf'))  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, prev_node, count):
        new_node = Node(count)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.freq_map[count] = new_node
        return new_node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.freq_map[node.count]
    
    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1
        
        curr_node = self.freq_map.get(count)
        next_node = self.freq_map.get(count + 1)
        
        if not next_node:
            next_node = self._add_node(self.head if not curr_node else curr_node, count + 1)
        next_node.keys.add(key)
        
        if curr_node:
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)
    
    def dec(self, key: str) -> None:
        count = self.key_count[key]
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
        
        curr_node = self.freq_map[count]
        prev_node = self.freq_map.get(count - 1)
        
        if count > 1 and not prev_node:
            prev_node = self._add_node(curr_node.prev, count - 1)
        if count > 1:
            prev_node.keys.add(key)
        
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)
    
    def getMaxKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.tail.prev.keys))
    
    def getMinKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))
