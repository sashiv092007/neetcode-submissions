class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         l = m
         r = n - 1
         i = 0
         while i < n:
            if nums1[l] == 0:
                nums1[l] = nums2[r]
                l += 1
                r -= 1
                i += 1
         return nums1.sort()    
