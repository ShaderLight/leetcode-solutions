from __future__ import annotations
from typing import Optional, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Parities:
    def __init__(self, other:Optional[Parities]=None) -> None:
        if not other:
            self.parities: Dict[int, int] = {}

            for i in range(9):
                self.parities[i+1] = 0
        
        else:
            self.parities = other.parities.copy()
    
    def addVal(self, val:int):
        if self.parities[val] == 0:
            self.parities[val] = 1
        
        else:
            self.parities[val] = 0
        
    def isPalindromic(self) -> int:
        return int(sum(self.parities.values()) <= 1)

    
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:      
        self.number_of_pp = 0
        self.pPP(root, Parities())
        
        return self.number_of_pp

    def pPP(self, node: Optional[TreeNode], parities:Parities):
        assert node
        parities.addVal(node.val)
        
        if not (node.left or node.right):
            self.number_of_pp += parities.isPalindromic()
            return

        if node.left:
            self.pPP(node.left, Parities(parities))

        if node.right:
            self.pPP(node.right, parities)
