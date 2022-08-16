from typing import List

class Solution:
    def __init__(self):
        self.values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        segments = self.splitSegments(s)
        print(segments)
        output = 0

        for seg in segments:
            if seg:
                if self.rToInt(seg[0]) >= self.rToInt(seg[-1]):
                    for c in seg:
                        output += self.rToInt(c)
                else:
                    assert len(seg) == 2
                    output += self.rToInt(seg[1]) - self.rToInt(seg[0])

        return output
    
    def splitSegments(self, s:str) -> List[str]:
        output: List[str] = []
        indexes: List[int] = []
        for i in range(len(s)-1):
            if s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                if i not in indexes:
                    indexes.append(i)
                indexes.append(i+2)

        if not indexes:
            return [s]

        output.append(s[:indexes[0]])

        for i in range(len(indexes)-1):
            output.append(s[indexes[i]:indexes[i+1]])

        output.append(s[indexes[-1]:])

        return output
            
    def rToInt(self, s:str) -> int:
        '''Integer value of single roman symbol'''
        assert len(s) == 1
        
        return self.values[s]


if __name__ == '__main__':
    obj = Solution()
    print(obj.romanToInt("MDCCCLXXXIV"))