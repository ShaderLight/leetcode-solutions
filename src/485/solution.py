from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        curr = 0
        for num in nums:
            if num:
                curr += 1
            else:
                curr_max = max(curr, curr_max)
                curr = 0
        
        return max(curr, curr_max)