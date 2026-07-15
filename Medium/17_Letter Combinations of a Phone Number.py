class Solution(object):
    def letterCombinations(self, digits:str):
        """
        :type digits: str
        :rtype: List[str]
        """
        combination = ['']
        if digits is None:
            return combination
        
        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',  
        }
 
        for digit in digits:
            new = []
            for combine in combination:
                for letter in keypad[digit]:
                    new.append(combine + letter)
            combination = new
        return combination
        

x = Solution()

hasil = x.letterCombinations('234')

print(hasil)