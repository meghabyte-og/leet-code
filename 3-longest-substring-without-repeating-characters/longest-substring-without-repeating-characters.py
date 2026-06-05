class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        d = {s[0] : 0}
        i = 0
        j = 1
        maxlen = 0
        while j < len(s) and i < j:

            if s[j] in d:
                i = max(i, d[s[j]] + 1)
        
            maxlen = max(maxlen, j - i + 1)
            d[s[j]] = j
            j = j + 1
            
        return maxlen
            
            


