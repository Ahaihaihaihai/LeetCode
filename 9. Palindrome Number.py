class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        mystr = str(x)[::-1]
        if mystr == str(x):
            return True
        else:
            return False