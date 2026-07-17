class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm = []
        nums.sort()
        def backtrack(combination, used):
            if len(combination) == len(nums):        
                perm.append(combination)
                return
            for i in range(len(nums)):
                if i > 0:
                    if nums[i] == nums[i-1] and i-1 not in used:
                        continue
                if i not in used:
                    backtrack(combination+[nums[i]], used+[i])
        backtrack([], [])
        return perm
    
x = Solution()
test1 = [1,2,3]
test2 = [1,1,2]
hasil = x.permuteUnique(test2)
print(hasil)