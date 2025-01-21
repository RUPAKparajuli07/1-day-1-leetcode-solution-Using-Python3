import random

class RandomizedSet:

    def __init__(self):
        # Dictionary to store value-to-index mapping
        self.val_to_index = {}
        # List to store the actual values
        self.values = []

    def insert(self, val: int) -> bool:
        # If the value already exists, return False
        if val in self.val_to_index:
            return False
        # Otherwise, add it to the list and map its index in the dictionary
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If the value doesn't exist, return False
        if val not in self.val_to_index:
            return False
        # Get the index of the value to remove
        idx_to_remove = self.val_to_index[val]
        # Swap the value with the last element in the list
        last_val = self.values[-1]
        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        # Remove the last element from the list
        self.values.pop()
        # Delete the value from the dictionary
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.values)
