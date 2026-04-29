class RecentCounter:
    # recentcounter=[]
    def __init__(self):
        self.recentcounter=[]

    def ping(self, t: int) -> int:
        count=0
        self.recentcounter.append(t)
        for i in self.recentcounter:
            if i>=t-3000:
                count+=1
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)