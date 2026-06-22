class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if max(nums) == 0:
            return "0"

        nums = list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return ''.join(nums)
                

        