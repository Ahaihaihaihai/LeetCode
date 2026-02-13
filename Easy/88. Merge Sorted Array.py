from time import sleep
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        p1 = m - 1
        p2 = n - 1
        p = m+n-1
        while p >= 0 and p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p >= 0 and p1 >= 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
            
        while p >= 0 and p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        return nums1

        
x = Solution()
print(x.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
print(x.merge([1,2,3,0,0,0], 3, [4,5,6], 3))
print(x.merge([1,3,5,0,0,0], 3, [2,4,6], 3))
print(x.merge([1], 1, [], 0))
print(x.merge([0], 0, [1], 1))