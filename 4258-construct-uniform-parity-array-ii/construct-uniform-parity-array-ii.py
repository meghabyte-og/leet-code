class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(nums1) <= 1:
            return True

        smallest = min(nums1)
        
        if smallest % 2 != 0:
            return True
        
        else:
            for num in nums1:
                if num%2 != 0:
                    return False
        
        return True

