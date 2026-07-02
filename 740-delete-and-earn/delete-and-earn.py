class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        house = [0] * ((max(nums))+1)
        for i in nums:
            house[i] += i
        if len(house) <= 2:
            return max(house)
        dp = [0]*len(house)

        dp[0] = house[0]
        dp[1] = house[1]
        dp[2] = house[0] + house[2]
        for i in range(3,len(dp)):
            dp[i] = house[i] + max(dp[i-3], dp[i-2])
        return max(dp[-1], dp[-2])