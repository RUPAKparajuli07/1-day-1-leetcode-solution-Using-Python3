class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        
        # If the total length is odd, find the (total_len // 2) + 1 th element
        if total_len % 2 == 1:
            return self.find_kth(nums1, nums2, total_len // 2 + 1)
        # If the total length is even, find the average of the (total_len // 2)th and (total_len // 2 + 1)th elements
        else:
            return (self.find_kth(nums1, nums2, total_len // 2) + self.find_kth(nums1, nums2, total_len // 2 + 1)) / 2
    
    def find_kth(self, nums1, nums2, k):
        # Ensure nums1 is always smaller or equal in length to nums2
        if len(nums1) > len(nums2):
            return self.find_kth(nums2, nums1, k)
        
        # If nums1 is empty, return the kth element of nums2
        if not nums1:
            return nums2[k - 1]
        
        # If k is 1, return the minimum of the first elements of nums1 and nums2
        if k == 1:
            return min(nums1[0], nums2[0])
        
        # Divide k into two parts, we will try to find elements up to k//2 in nums1 and nums2
        part_nums1 = min(k // 2, len(nums1))
        part_nums2 = k - part_nums1
        
        # If the k//2th element of nums1 is smaller than the k//2th element of nums2,
        # we can discard the first part of nums1 and vice versa
        if nums1[part_nums1 - 1] < nums2[part_nums2 - 1]:
            return self.find_kth(nums1[part_nums1:], nums2, k - part_nums1)
        else:
            return self.find_kth(nums1, nums2[part_nums2:], k - part_nums2)
