class Solution:
    def merge(self, nums1: List[int], M: int, nums2: List[int], N: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i, j, k = M - 1, N - 1, M + N -1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while i >= 0:
            nums1[k] = nums1[i]
            i, k = i -1, k - 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j, k = j - 1, k - 1
            
        
            