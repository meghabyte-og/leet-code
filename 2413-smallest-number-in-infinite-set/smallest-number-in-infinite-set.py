import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.minheap = []
        self.intset = set()
        for i in range(1,1001): 
            heapq.heappush(self.minheap, i)  
            self.intset.add(i)  
        
    def popSmallest(self) -> int:
        curr = heapq.heappop(self.minheap)
        self.intset.discard(curr)
        return curr 

    def addBack(self, num: int) -> None:
        if num not in self.intset:
            heapq.heappush(self.minheap, num)
            self.intset.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)