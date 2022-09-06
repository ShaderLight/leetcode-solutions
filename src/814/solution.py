from __future__ import annotations
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: Optional[TreeNode]=None, right: Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        if not self.left:
            l = None
        else:
            l = self.left.val

        if not self.right:
            r = None
        else:
            r = self.right.val
        
        return f'[{l}]<-[{self.val}]->[{r}]'


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if (not root.left) and (not root.right) and (root.val == 0):
            return None
        
        return root


def treeTraversalUtil(root:TreeNode) -> None:
    def printNode(root:TreeNode) -> None:
        l_val = root.left.val if root.left else None
        r_val = root.right.val if root.right else None
        print('Current node')
        print(f'   {root.val}\n{l_val}    {r_val}')
    
    command = -1
    current_node = root
    traversal_history: List[TreeNode] = []

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

    # [1, null, 0, 0, 1]
    root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
    pruned = obj.pruneTree(root)
    # Should yield [1, null, 0, null, 1]
    
    assert pruned
    treeTraversalUtil(pruned)
