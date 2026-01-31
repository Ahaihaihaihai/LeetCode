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
        if mylen % 2 == 1:
            return nums3[mylen]
        else:
            return (nums3[mylen] + nums3[mylen+1]) / 2
