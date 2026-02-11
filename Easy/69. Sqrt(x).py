class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left = 0
        right = x
        mid = (right - left) // 2
        count = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
        if mid ** 2 > x:
            return mid - 1
        else:
            return mid
        
x = Solution()
print(x.mySqrt(8))
print(x.mySqrt(4))
print(x.mySqrt(10))
print(x.mySqrt(100))
print(x.mySqrt(81))