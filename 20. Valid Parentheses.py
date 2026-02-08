class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = list('')
        for i in range(len(s)):
            if s[i] == '(':
                check.append(')')
            elif s[i] == '{':
                check.append('}')
            elif s[i] == '[':
                check.append(']')
            else:
                test = check.pop() if check else 'a'
                if s[i] != test:
                    return False
                
        if check:
            return False
        else:
            return True