from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def halfUtil(self, a:int, b:int=0):
        return (a+b)//2

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        mid = self.halfUtil(len(nums))

        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))


def treeTraversalUtil(root:TreeNode) -> None:
    def printNode(root:TreeNode) -> None:
        l_val = root.left.val if root.left else None
        r_val = root.right.val if root.right else None
        print('Current node')
        print(f'   {root.val}\n{l_val}    {r_val}')
    
    command = -1
    current_node = root
    traversal_history = []

    while command != -2:
        printNode(current_node)
        command = int(input('\nInput 1 to traverse left, 2 to traverse right, 3 to go back, 4 to end.\n'))

        match command:
            case 1:
                if current_node.left:
                    traversal_history.append(current_node)
                    current_node = current_node.left
                else:
                    print('Cannot traverse further!')
            case 2:
                if current_node.right:
                    traversal_history.append(current_node)
                    current_node = current_node.right
                else:
                    print('Cannot traverse further!')
            case 3:
                try:
                    current_node = traversal_history.pop()
                except IndexError:
                    print('Nothing to go back to!')
            case 4:
                command = -2
            case _:
                print('Invalid command!')




if __name__ == '__main__':
    obj = Solution()
    result = obj.sortedArrayToBST([-10,-3,0,5,9])
    treeTraversalUtil(result)