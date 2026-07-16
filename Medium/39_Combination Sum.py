class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        hasil = []
        def backtrack(combination, target, index):
            if target == 0:
                hasil.append(combination)
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                backtrack(combination + [candidates[i]], target - candidates[i], i)
        
        backtrack([], target, 0)
        return hasil
    
x = Solution()
hasil = x.combinationSum([2,3],8)
print(hasil)