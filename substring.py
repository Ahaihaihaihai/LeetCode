class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = slen = 0
        mystr = set()

        for right in range(len(s)):
            while s[right] in mystr:
                mystr.remove(s[left])
                left += 1
            
            mystr.add(s[right]) 
            slen = max(slen, right - left + 1)
        return slen