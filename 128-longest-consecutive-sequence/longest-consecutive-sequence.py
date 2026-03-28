import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxlen=0
        
        for i in s:
            length=1
            if i-1 not in s: 
                while i+1 in s:
                    length+=1
                    i+=1
            maxlen=max(length,maxlen)
        return maxlen

