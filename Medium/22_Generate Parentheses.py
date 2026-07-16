class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        def backtrack(string, open_count, close_count):
            if open_count == n and close_count == n:
                answer.append(string)
                return
            if open_count < n:
                backtrack(string + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(string + ')', open_count, close_count+1)

        backtrack("", open_count=0, close_count=0)
        return answer
           

x = Solution()
hasil = x.generateParenthesis(3)

print(hasil)