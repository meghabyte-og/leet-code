class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        m, n = len(nums1), len(nums2)
        total_len = m + n
        mid_idx = total_len // 2
        
        p1, p2 = 0, 0
        curr_val, prev_val = 0, 0
        for _ in range(mid_idx + 1):
            prev_val = curr_val
            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                curr_val = nums1[p1]
                p1 += 1
            else:
                curr_val = nums2[p2]
                p2 += 1
        if total_len % 2 != 0:
            return float(curr_val)
        else:
            return (prev_val + curr_val) / 2.0
