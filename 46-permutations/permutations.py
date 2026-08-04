class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(curr, rem) -> None:
            if len(rem) == 0:
                result.append(curr)
                return
            for i in range(len(rem)):
                backtrack(curr+[rem[i]], rem[:i]+rem[i+1:])
            return
        backtrack([], nums)
        return result
            