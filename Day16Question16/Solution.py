class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to simplify the process
        
        closest_sum = float('inf')  # Initialize closest sum to positive infinity
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return target  # Found exact match, return target sum
                
                # Update closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on whether the current sum is smaller or larger than the target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum  # Return the closest sum found

# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))  # Output: 2
print(solution.threeSumClosest([0,0,0], 1))     # Output: 0
