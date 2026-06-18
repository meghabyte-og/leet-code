class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        mangle = minutes * 6
        hangle = hour*30 + minutes*0.5
        return min(abs(hangle - mangle),360-abs(hangle-mangle))
       
