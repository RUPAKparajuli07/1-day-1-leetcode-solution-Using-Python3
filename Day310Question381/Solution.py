import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        # List to store elements
        self.elements = []
        # Dictionary to map values to their indices in the list
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.elements.append(val)
        self.indices[val].add(len(self.elements) - 1)
        # Return True if val was not already present
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        # Get an arbitrary index of the value to remove
        remove_index = self.indices[val].pop()
        last_element = self.elements[-1]

        # Move the last element to the position of the element to remove
        self.elements[remove_index] = last_element
        # Update the dictionary for the last element
        self.indices[last_element].add(remove_index)
        self.indices[last_element].discard(len(self.elements) - 1)

        # Remove the last element from the list
        self.elements.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)

# Example Usage:
# randomizedCollection = RandomizedCollection()
# print(randomizedCollection.insert(1))  # True
# print(randomizedCollection.insert(1))  # False
# print(randomizedCollection.insert(2))  # True
# print(randomizedCollection.getRandom())  # Randomly returns 1 or 2
# print(randomizedCollection.remove(1))  # True
# print(randomizedCollection.getRandom())  # Randomly returns 1 or 2
