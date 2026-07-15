class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                width = abs(i-j)
                hasil = width * min(height[i], height[j])
                if max < hasil:
                    max = hasil
        return max