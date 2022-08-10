from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: len(str(x))%2==0, nums))