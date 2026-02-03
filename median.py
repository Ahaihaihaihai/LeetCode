class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # nums3 = sorted(nums1 + nums2)
        # mylen = len(nums3)

        # if mylen % 2 ==0:
        #     return (nums3[mylen//2] + nums3[(mylen//2) + 1])/2.0
        # else:
        #     return nums3[mylen//2]
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        lenA, lenB = len(nums1), len(nums2)
        left, right = 0, lenA

        while left <= right:
            part1 = (left + right) // 2
            part2 = (lenA + lenB + 1) // 2 - part1

            max_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            min_right1 = float('inf') if part1 == lenA else nums1[part1]
            max_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            min_right2 = float('inf') if part2 == lenB else nums2[part2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (lenA + lenB) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return max(max_left1,max_left2)
            elif max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1
                
