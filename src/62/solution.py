from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2)/ (factorial(m - 1) * factorial(n - 1)))

obj = Solution()
print(obj.uniquePaths(3, 7))