class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        d={}
        maxlen=0
        for right in range(len(s)):
            if s[right] in d:
                # print(left,d[s[right]]+1)
                left=max(left,d[s[right]]+1)
            # print(s[left:right+1])
            d[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen