from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i):
            return (i + nums[i]) % n  # Ensure circular movement
        
        for i in range(n):
            if nums[i] == 0:  # Skip visited elements
                continue
            
            slow, fast = i, next_index(i)

            # Check for cycle using slow and fast pointers
            while (nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0):
                if slow == fast:  # Cycle detected
                    if slow != next_index(slow):  # Cycle length > 1
                        return True
                    else:
                        break  # Single-element cycle, not valid
                
                # Move pointers
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Mark all visited elements in this path as 0
            marker = i
            while nums[marker] * nums[next_index(marker)] > 0:
                temp = marker
                marker = next_index(marker)
                nums[temp] = 0  # Mark as visited
        
        return False
