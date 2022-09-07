from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def t2sHelper(root: Optional[TreeNode]) -> str:
            if not root:
                return ''

            r = f'({t2sHelper(root.right)})' if root.right else ''
            
            l = f'({t2sHelper(root.left)})' if root.left else '()'
            
            if l == '()' and not root.right:
                l = ''
            
            return f'{root.val}{l}{r}'
        
        return t2sHelper(root)