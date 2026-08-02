class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recurse(start, end):
            if start > end:
                return 0
            return max(
                nums[start] - recurse(start+1, end),
                nums[end] - recurse(start, end-1)
            )
        dp = recurse(0, len(nums)-1)
        return True if dp >=0 else False
            
