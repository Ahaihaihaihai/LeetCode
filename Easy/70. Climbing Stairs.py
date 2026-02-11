class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        prev1 = 2
        prev2 = 3

        for _ in range(3, n):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        return cur
x = Solution()
print(x.climbStairs(2))
print(x.climbStairs(3))