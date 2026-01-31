class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        mylen = len(nums3)
        target = mylen//2
        if mylen % 2 == 1:
            return nums3[target]
        else:
            return (nums3[target] + nums3[target]) / 2
