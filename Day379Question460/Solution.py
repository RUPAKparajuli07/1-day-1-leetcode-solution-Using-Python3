from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}  # Stores key-value pairs
        self.key_to_freq = {}  # Stores key-frequency pairs
        self.freq_to_keys = defaultdict(OrderedDict)  # Frequency to OrderedDict of keys
        self.min_freq = 0  # Minimum frequency tracker

    def _update_freq(self, key):
        """Updates the frequency of the given key."""
        freq = self.key_to_freq[key]
        value = self.key_to_val[key]
        
        # Remove key from current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:  # If no keys left, remove frequency bucket
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1  # Update min_freq if needed
        
        # Add key to the next frequency list
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = value

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_val:
            # Update the value and frequency
            self.key_to_val[key] = value
            self._update_freq(key)
            return
        
        if len(self.key_to_val) >= self.capacity:
            # Evict the LFU key (if tie, LRU among them)
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[lfu_key]
            del self.key_to_freq[lfu_key]

        # Insert new key with frequency 1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1  # Reset min_freq

