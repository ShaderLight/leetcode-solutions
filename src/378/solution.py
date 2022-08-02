from typing import*
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_val, max_val = matrix[0][0], matrix[-1][-1]

        while min_val < max_val:
            mid_val = self.halfUtil(min_val, max_val)

            smaller_count = self.howManySmaller(matrix, mid_val)

            if smaller_count < k:
                min_val = mid_val + 1
            else:
                max_val = mid_val

        return min_val

    def howManySmaller(self, matrix, val):
        count = 0
        for row in matrix:
            count += bisect.bisect_right(row, val)

        return count

    def halfUtil(self, s, e):
        return (s+e)//2

obj = Solution()

print(obj.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))