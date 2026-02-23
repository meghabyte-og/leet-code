class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in range(len(strs)):
            s=tuple(sorted(strs[i]))
            if s not in seen:
                seen[s]=[]
            seen[s].append(strs[i])
        return list(seen.values())