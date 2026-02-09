class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a=0
        n=len(candidates)
        subsets=[]
        current=[]
        s=sum(candidates)
        def sub(a,i):
            if a==target and current[:] not in subsets:
                subsets.append(current[:])
                return
            if a>target:
                return
            if i>=n:
                return
            a=a+candidates[i]
            current.append(candidates[i])
            sub(a,i+1)
            sub(a,i)
            a=a-candidates[i]
            if current:
                current.pop()
            sub(a,i+1)
            
        sub(a,0)
        return subsets

            


                



