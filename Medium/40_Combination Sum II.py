class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        hasil = []
        def backtrack(combination, target, index):
            if target == 0:
                if combination in hasil:
                    return
                else:
                    hasil.append(combination)
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                backtrack(combination + [candidates[i]], target - candidates[i], i + 1)
        
        backtrack([], target, 0)
        return hasil


x = Solution()
hasil = x.combinationSum2([10,1,2,7,6,1,5], 8)
print(hasil)
