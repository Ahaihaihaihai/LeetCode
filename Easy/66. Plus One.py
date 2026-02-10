class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
            

x = Solution()
print(x.plusOne([1,2,3]))
print(x.plusOne([4,3,2,1]))
print(x.plusOne([9]))
print(x.plusOne([9,9,9]))