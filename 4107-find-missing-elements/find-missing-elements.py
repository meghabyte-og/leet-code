class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        original = [i for i in range(min(nums), max(nums)+1)]
        j = 0
        result = []
        nums = sorted(nums)
        for i in range(len(original)):
            if j == len(nums):
                result = result + original[i:]
                return result
            if original[i] == nums[j]:
                j = j + 1
            else:
                result.append(original[i])
        return result

