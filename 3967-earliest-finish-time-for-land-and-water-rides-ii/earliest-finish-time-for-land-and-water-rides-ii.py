class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        minimum = float('inf')
        #first land then water 
        # pairs = sorted(zip(landStartTime, landDuration))
        # landStartTime = [a for a, b in pairs]
        # landDuration = [b for a, b in pairs]

        min_landEndTime = min([a+b for a,b in zip(landStartTime, landDuration)])
        
        #what's the next earliest ending water time?
        for i in range(len(waterDuration)):
            if waterStartTime[i] >= min_landEndTime: 
                minimum = min(minimum, waterStartTime[i] + waterDuration[i])
            else: 
                minimum = min(minimum, min_landEndTime + waterDuration[i])



        min_waterEndTime = min([a+b for a,b in zip(waterStartTime, waterDuration)])

        for i in range(len(landDuration)):
            if landStartTime[i] >= min_waterEndTime: 
                minimum = min(minimum, landStartTime[i] + landDuration[i])
            else: 
                minimum = min(minimum, min_waterEndTime + landDuration[i])
        return minimum




        
        
