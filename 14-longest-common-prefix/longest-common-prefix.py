class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #[0][0], [1][0], [2][0]
        #[0][1], [1][1], [2],[1]
        first=strs[0]
        for i in range(1,len(strs)):
            if strs[i]==first:
                first=strs[i]
                continue
            else:
                while not strs[i].startswith(first):
                    first=first[:-1]
                    if first=='':
                        return ''
                
        return first
                
