class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                result.append(s[i])
            else:
                if s[i] == '*':
                    if len(result)!=0:
                        result.pop()

                elif s[i] == '#':
                    result = result + result
                else:
                    result = result[::-1]
        return ''.join(result)
