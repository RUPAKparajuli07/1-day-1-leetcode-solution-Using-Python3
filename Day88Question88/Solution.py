from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1, nums2, and the end of the merged array
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
