from typing import List

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        
        def ithRow(i: int) -> List[int]:
            prev = dp[i-1]
            return [prev[1] + prev[2] + prev[4], prev[0] + prev[2], prev[1] + prev[3], prev[2], prev[2] + prev[3]]

        # Initializing 2d dp array of size 5 X n
        dp = [[0]*5 for _ in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        
        # VOWELS = ('a', 'e', 'i', 'o', 'u')
        #            0    1    2    3    4

        # VOWELS_RULES = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        #               'a'    'e'        'i'       'o'    'u'


        
        for i in range(1, n):
            dp[i] = ithRow((i))
                



        return sum(dp[n-1]) % (10**9 + 7)



if __name__ == '__main__':
    obj = Solution()
    print(obj.countVowelPermutation(1))