class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        zero = 0
        for i in nums:
            if i == 0 :
                zero +=1
            if zero == len(nums):
                return "0"
            i = str(i)
        if len(nums) == 1:
            return str(nums[0])

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                if int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i])):
                    nums[j], nums[i] = nums[i], nums[j]
        return ''.join([str(i) for i in nums])
                

        