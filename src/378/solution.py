from typing import List
from bisect import bisect_right

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_val, max_val = matrix[0][0], matrix[-1][-1]

        while min_val < max_val:
            mid_val = self.halfUtil(min_val, max_val)

            smaller_count = self.kSmaller(matrix, mid_val)

            if smaller_count < k:
                min_val = mid_val + 1
            else:
                max_val = mid_val

        return min_val

    def kSmaller(self, matrix: List[List[int]], val: int) -> int:
        count = 0
        for row in matrix:
            count += bisect_right(row, val)

        return count

    def halfUtil(self, s: int, e: int) -> int:
        return (s+e)//2


if __name__=='__main__':
    # Example driver code
    obj = Solution()
    print(obj.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)) 
    # Should yield 13