from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        skip = False
        for i in range(len(arr)-1):
            if skip:
                skip = False
                continue
            if arr[i] == 0:
                skip = True
                temp = 0
                temp2 = 0
                for j in range(i+1, len(arr)):
                    temp2 = arr[j]
                    arr[j] = temp
                    temp = temp2


if __name__ == '__main__':
    obj = Solution()
    arr = [1,0,2,3,0,4,5,0]
    obj.duplicateZeros(arr)
    print(arr)