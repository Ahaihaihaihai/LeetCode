class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # mystr = str(x)[::-1]
        # if mystr == str(x):
        #     return True
        # else:
        #     return False
        if x < 0:
            return False
        
        copy = x
        reverse = 0
        
        while copy > 0:
            reverse = (reverse * 10) + (copy % 10)
            copy //= 10
        return reverse == x