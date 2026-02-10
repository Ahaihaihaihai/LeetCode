class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count = last = 0
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         count += 1
        #     else:
        #         if s[i:] == ' ' * (len(s) - i):
        #             return count
        #         else:
        #             count = 0
        # return count
        end = len(s) - 1

        while s[end] == ' ':
            end -= 1

        start = end
        while s[start] != ' ' and start >= 0:
            start -= 1

        return end - start    
    
x = Solution()
print(x.lengthOfLastWord("Hello World"))
print(x.lengthOfLastWord("   fly me   to   the moon  "))
print(x.lengthOfLastWord("luffy is still joyboy"))