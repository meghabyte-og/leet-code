class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recurse(target, sub, start):

            if target == 0:
                result.append(sub[:])
                return
            
            if target < 0:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sub.append(candidates[i])
                recurse(target - candidates[i], sub, i+1)
                sub.pop()
        
        recurse(target, [], 0)
        return result

            
