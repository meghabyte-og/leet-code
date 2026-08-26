class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [0]*n
        def recurse(i, points):
            if i > n-1:
                return 0 
            if memo[i] != 0:
                return memo[i]
            memo[i] = max(
                questions[i][0] + recurse(i+questions[i][1]+1, points + questions[i][0]), recurse(i+1, points)
                )
            return memo[i]
        return recurse(0, 0)