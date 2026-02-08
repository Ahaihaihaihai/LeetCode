class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = list('')
        for char in s:
            if char == '(':
                check.append(')')
            elif char == '{':
                check.append('}')
            elif char == '[':
                check.append(']')
            else:
                test = check.pop() if check else 'a'
                if char != test:
                    return False
                
        if check:
            return False
        else:
            return True