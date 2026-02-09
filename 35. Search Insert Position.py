class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (right - left) // 2
        if target > max(nums):
            return len(nums)
        if target >= nums[mid] or target <= nums[mid + 1]:
            return mid if target == nums[mid] else mid + 1
        elif target >= nums[mid]:
            return self.searchInsert(nums[mid:right],target)
        elif target <= nums[mid]:
            return self.searchInsert(nums[left:mid], target)
        
        