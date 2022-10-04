from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:Optional[TreeNode]=None, right:Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if (targetSum - root.val) == 0:
            if root.left == None and root.right == None:
                return True

        if root.left != None and root.right != None:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        if root.left != None:
            return self.hasPathSum(root.left, targetSum - root.val)
        if root.right != None:
            return self.hasPathSum(root.right, targetSum - root.val)

        return False

if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
    print(obj.hasPathSum(root, -1))