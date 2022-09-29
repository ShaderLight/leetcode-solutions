from typing import List
from bisect import insort

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        def binarySearch(arr: List[int], x: int, l: int, r: int) -> int:
            def half(a: int, b: int=0) -> int:
                assert a >= 0 and b >= 0
                return abs(a+b)//2
            
            if l == r:
                return l
            
            mid = half(l, r)
            
            if arr[mid] < x:
                return binarySearch(arr, x, mid+1, r)
            
            return binarySearch(arr, x, l, mid)
        
        def compareDistance(a: int, b:int, x:int) -> bool:
            if (abs(a-x) < abs(b-x)):
                return True
            
            if (abs(a-x) == abs(b-x)) and (a < b):
                return True

            return False
        
        ptr = binarySearch(arr, x, 0, N-1)
        try:
            if compareDistance(arr[ptr-1], arr[ptr], x) and ptr-1 >= 0:
                ptr -= 1
        except:
            pass
    
        ptr1 = -1
        ptr2 = N
        output = [arr[ptr]]

        if ptr - 1 >= 0:
            ptr1 = ptr - 1
        
        if ptr + 1 < N:
            ptr2 = ptr + 1

        while len(output) < k:
            if ptr1 >= 0 and ptr2 < N:
                if compareDistance(arr[ptr1], arr[ptr2], x):
                    insort(output, arr[ptr1])
                    ptr1 -= 1
                else:
                    insort(output, arr[ptr2])
                    ptr2 += 1
            
            elif ptr1 >= 0:
                insort(output, arr[ptr1])
                ptr1 -= 1
            
            else:
                insort(output, arr[ptr2])
                ptr2 += 1

        return output





if __name__ == '__main__':
    obj = Solution()
    #print(obj.findClosestElements([1,2,3,3,4,4,4,5], 4, 3))

    print(obj.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))