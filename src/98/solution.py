from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_condition = self.traverseAndCompare(root.left, root.val, False)
        right_condition = self.traverseAndCompare(root.right, root.val, True)
        
        return left_condition and right_condition and self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def traverseAndCompare(self, root: Optional[TreeNode], x:int, greater: bool) -> bool:
        if not root:
            return True
        
        if greater:
            return root.val > x and self.traverseAndCompare(root.left, x, greater) and self.traverseAndCompare(root.right, x, greater)
        
        return root.val < x and self.traverseAndCompare(root.left, x, greater) and self.traverseAndCompare(root.right, x, greater)