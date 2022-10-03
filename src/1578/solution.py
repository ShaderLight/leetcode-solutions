from typing import List
from bisect import insort

class SmallestContainer:
    def __init__(self, size:int):
        self.size = size
        self.arr: List[int] = []
        self.length = 0

    def put(self, x:int) -> None:
        if self.size == 1 and self.length >= 1:
            if self.arr[0] > x:
                self.arr[0] = x
                return
            else:
                return
    
        if self.length >= self.size:
            if self.arr[-1] < x:
                return
            self.arr.pop()
            insort(self.arr, x)
            self.length += 1
            return

        insort(self.arr, x)
        self.length += 1

    def summarise(self):
        return sum(self.arr)

    def __repr__(self) -> str:
        return str(self.arr)

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        group_len = 1
        output = 0
        N = len(colors)

        for i in range(1, N):
            if colors[i-1] == colors[i]:
                group_len += 1
            else:
                if group_len > 1:
                    output += self.sumNsmallest(neededTime, group_len - 1, i - group_len, i-1)
                    group_len = 1

        if group_len > 1:
            output += self.sumNsmallest(neededTime, group_len - 1, N - group_len, N - 1)
        
        return output

            
    def sumNsmallest(self, neededTime: List[int], n: int, l:int, r:int) -> int:
        assert (r - l + 1) >= n 
        
        container = SmallestContainer(n)
        
        for i in range(l, r+1):
            container.put(neededTime[i])

        return container.summarise()

if __name__ == '__main__':
    obj = Solution()
    print(obj.minCost("bbbaaa", [4,9,3,8,8,9]))