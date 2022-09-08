from __future__ import annotations
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output: List[int] = []

        def iTHelper(root: Optional[TreeNode], vals:List[int]):
            if not root:
                return

            iTHelper(root.left, vals)
            vals.append(root.val)
            iTHelper(root.right, vals)


        iTHelper(root, output)

        return output
