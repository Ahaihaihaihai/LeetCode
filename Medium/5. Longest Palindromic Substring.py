class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        start = end = 0
        
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            max_len = max(odd,even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len //2   
        return s[start:end+1]