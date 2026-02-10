class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in range(len(strs)):
            key=tuple(sorted(strs[i]))
            if key not in seen:
                seen[key]=[strs[i]]
            else:
                seen[key].append(strs[i])
        return list(seen.values()) 

            
            
            
            

            