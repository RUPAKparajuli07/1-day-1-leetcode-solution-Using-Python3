from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings for easy concatenation
        nums_str = list(map(str, nums))

        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Join the sorted strings
        largest_num = ''.join(nums_str)

        # Handle the case where the largest number is 0
        if largest_num[0] == '0':
            return '0'

        return largest_num
