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
                hasil.append(combination)
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                if candidates[i] == candidates[i-1] and index < i:
                    continue
                backtrack(combination + [candidates[i]], target - candidates[i], i + 1)
        
        backtrack([], target, 0)
        return hasil


x = Solution()
mylist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
mylist2 = [10,1,2,7,6,1,5]
hasil = x.combinationSum2(mylist, 27)
print(hasil)
