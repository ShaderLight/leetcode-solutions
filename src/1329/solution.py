from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        M = len(mat[0])
        N = len(mat)
        
        for i in range(M):
            self.sortOneDiagonal(mat, i, 0)
            
        for i in range(1, N):
            self.sortOneDiagonal(mat, 0, i)
            
        return mat
            
        
    
    def sortOneDiagonal(self, mat: List[List[int]], x: int, y: int) -> None:
        temp: List[int] = []
        x_temp = x
        y_temp = y
        
        while True:
            try:
                temp.append(mat[y_temp][x_temp])
            except IndexError:
                break
            x_temp += 1
            y_temp += 1
            
        temp.sort()
        
        for i in range(len(temp)):
            mat[y+i][x+i] = temp[i]

if __name__ == '__main__':
    obj = Solution()
    print(obj.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    # Should yield [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
