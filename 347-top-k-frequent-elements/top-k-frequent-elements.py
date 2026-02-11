class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        final=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1
        seen=dict(sorted(seen.items(), key=lambda item: item[1])[::-1])
        
        seenlist=list(seen.items())
        for i in range(k):
            final.append(seenlist[i][0])
        return final