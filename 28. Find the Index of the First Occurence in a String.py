class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = i = rem = 0
        while i < len(haystack):
            if haystack[i] == needle[index]:
                index += 1
                if index == len(needle):
                    return i - (index - 1)
                i+=1
            else:
                i -= index
                index = 0
                i+=1
        return -1