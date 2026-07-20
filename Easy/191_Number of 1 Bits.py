class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## String count method
        # def int_to_bin(n):
        #     biner = ''
        #     while n > 0:
        #         sisa = n % 2
        #         biner = str(sisa) + biner
        #         n = n // 2
        #     return biner
        
        # biner = int_to_bin(n)
        # return biner.count('1')
    
        ## Binary Operator Method
        weight = 0
        while n:
            weight += n&1
            n = n >> 1
        return weight

x = Solution()
print(x.hammingWeight(2147483645))