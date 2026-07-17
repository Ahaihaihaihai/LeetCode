class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm = []
        def backtrack(combination, used):
            if len(combination) == len(nums):
                if combination in perm:
                    return
                else:
                    perm.append(combination)
                    return
            for i in range(len(nums)):
                if i not in used:
                    backtrack(combination+[nums[i]], used+[i])
        backtrack([], [])
        return perm
    
x = Solution()
test1 = [1,2,3]
test2 = [1,1,2]
hasil = x.permuteUnique(test2)
print(hasil)