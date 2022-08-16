from typing import List, Dict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        trees_with_root: Dict[int, int] = {}

        for x in arr:
            trees_with_root[x] = 1
        
        for i in range(1, len(arr)):
            for j in range(i):
                possible_child_node = arr[i] // arr[j]

                if possible_child_node < 2:
                    break
                if arr[i] % arr[j] != 0:
                    continue
                
                trees_with_root[arr[i]] += trees_with_root.get(possible_child_node, 0) * trees_with_root[arr[j]]

        return sum(trees_with_root.values()) % (10**9 + 7)


if __name__ == '__main__':
    obj = Solution()
    print(obj.numFactoredBinaryTrees([2,4]))