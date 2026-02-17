class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result=[]
        led=[1,2,4,8, 1,2,4,8,16,32]
        def recurse(index,count,hour,minute):
            if hour>11 or minute>59:
                return
            if count==turnedOn:
                result.append(str(hour) + ":" + (str(minute) if minute >= 10 else "0" + str(minute)))

                return
            for i in range(index,len(led)):
                if i<4:
                    recurse(i+1,count+1,hour+led[i],minute)
                else:
                    recurse(i+1,count+1,hour,minute+led[i])
        recurse(0,0,0,0)
        return(result)