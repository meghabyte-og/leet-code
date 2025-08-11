class Solution:
    def compress(self, chars: List[str]) -> int:
        p=0
        count=1
        for i in range(1, len(chars)+1):
            if i==len(chars) or chars[i]!=chars[i-1]:
                chars[p]=chars[i-1]
                p=p+1
                if count>1:
                    count_str=str(count)
                    for j in range(len(count_str)):
                        chars[p]=count_str[j]
                        p=p+1
                    count=1
            else:
                count+=1
        chars[:]=chars[:p]
        return p