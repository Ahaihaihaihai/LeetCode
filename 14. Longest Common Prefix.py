class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = ""
        shortest = min(len(s) for s in strs)

        for i in range(shortest):
            ch = strs[0][i]
            for j in strs:
                if j[i] != ch:
                    return prefix    
            prefix += ch
        return prefix