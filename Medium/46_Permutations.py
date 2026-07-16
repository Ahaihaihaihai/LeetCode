class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        hasil = []
        def backtrack(combination):
            if len(combination) == len(nums):
                hasil.append(combination)
                return
            for i in range(len(nums)):
                if nums[i] not in combination:
                    backtrack(combination+[nums[i]])
        backtrack([])
        return hasil
    

        
x = Solution()
test1 = [1,2,3]
test2 = [0,1]
test3 = [1]
test4 = []
hasil = x.permute(test4)
print(hasil)
