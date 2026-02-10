from time import sleep

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
            print(f'L: {left}, R:{right}, M:{mid}')
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                mid = mid + 1
            elif mid ** 2 > x:
                mid = mid - 1
            sleep(0.5)
            
x = Solution()
print(x.mySqrt(100))