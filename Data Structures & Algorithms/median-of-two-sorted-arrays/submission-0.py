class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        median = 0

        if n % 2 != 0:
            index = int((n + 1) / 2) - 1
            median = merged[index]
        else:
            index1 = int((n / 2) - 1)
            index2 = int((n / 2))
            pos1 = merged[index1]
            pos2 = merged[index2]
            average = (pos1 + pos2) / 2
            median = average

        return median
