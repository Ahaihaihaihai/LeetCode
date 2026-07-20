class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def int_to_bin(n):
            biner = ''
            while n > 0:
                sisa = n % 2
                biner = str(sisa) + biner
                n = n // 2
            return biner
        
        def bin_to_int(s):
            count = 1
            hasil = 0
            for i in range(len(s)):
                hasil += count * int(s[-(i+1)])
                count *= 2
            return hasil
        
        biner = int_to_bin(n)
        biner = biner.zfill(32)
        new = ''
        for i in biner:
            new = i + new
        return bin_to_int(new)
    
x = Solution()
hasil = x.reverseBits(43261596)
print(hasil)