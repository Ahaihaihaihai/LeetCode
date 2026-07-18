class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combination = []
        def backtrack(input, start=1):
            if len(input) == k:
                combination.append(input)
                return
            for i in range(start,n+1):
                backtrack(input+[i],i+1)
        backtrack([],1)
        return combination

x = Solution()
hasil = x.combine(4,2)
print(hasil)
