class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high=0
        current_altitude=0
        for i in range(len(gain)):
            current_altitude+=gain[i]           
            high=max(high,current_altitude)
        return high