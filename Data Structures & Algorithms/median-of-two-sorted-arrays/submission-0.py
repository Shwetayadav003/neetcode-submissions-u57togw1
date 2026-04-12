class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = nums1 + nums2
        final.sort()
        n = len(final)
        if n % 2 == 1:
            median = final[n // 2]
        else:
            median = (final[n // 2 - 1]+  final[n // 2]) / 2
        return median
        