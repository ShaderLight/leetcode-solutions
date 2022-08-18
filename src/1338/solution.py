from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        halfN = len(arr)//2
        occurences: dict[int, int] = {}
        
        for num in arr:
            try:
                occurences[num] += 1
            except KeyError:
                occurences[num] = 1
                
        sorted_occurences = sorted(occurences.items(), key=lambda item: item[1], reverse=True)
        print(sorted_occurences)
        
        output: set[int] = set()
        newN = N
        for entry in sorted_occurences:
            newN -= entry[1]
            output.add(entry[0])
            if newN <= halfN:
                break
        
        return len(output)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minSetSize([3,3,3,3,5,5,5,2,2,7]))
    # Should yield 2