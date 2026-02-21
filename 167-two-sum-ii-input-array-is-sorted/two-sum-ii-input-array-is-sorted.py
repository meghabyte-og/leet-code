class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            
            c=target-numbers[i]
            if c not in seen:
                seen[numbers[i]]=i
            else:
                return [seen[c]+1,i+1]
        return []
