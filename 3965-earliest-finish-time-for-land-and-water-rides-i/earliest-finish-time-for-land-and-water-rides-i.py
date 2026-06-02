class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_end = waterStartTime[j] + waterDuration[j]

                finish1 = max(land_end, waterStartTime[j]) + waterDuration[j]

                finish2 = max(water_end, landStartTime[i]) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans