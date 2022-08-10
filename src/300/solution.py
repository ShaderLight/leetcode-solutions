from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.subseq = [nums.pop(0)]

        for num in nums:
            if num > self.subseq[-1]:
                self.subseq.append(num)
            else:
                self.subseq[self.leftmostBinarySearch(num, 0, len(self.subseq))] = num
        

        print(self.subseq)
        return len(self.subseq)

    def leftmostBinarySearch(self, x:int, l:int, r:int) -> int:
        def half(a:int, b:int=0) -> int:
            return(a+b)//2

        while l != r:
            mid = half(l, r)
            if self.subseq[mid] < x:
                l = half(l, r) + 1
            else:
                r = half(l, r)

        return l

if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLIS([0, 1, 2, 5, 6, 3]))