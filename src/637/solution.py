from __future__ import annotations
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left: Optional[TreeNode]=None, right: Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'TreeNode({self.val})'

import queue

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q: queue.Queue[TreeNode] = queue.Queue()
        q_len = 0
        temp: List[TreeNode] = []
        output: List[float] = []
        temp_avg = 0
        
        assert root
        
        q.put(root)
        
        while not q.empty():
            while not q.empty():
                node = q.get()
                if not node:
                    continue
                
                q_len += 1
                temp_avg += node.val
                
                if node.left:
                    temp.append(node.left)
                    
                if node.right:
                    temp.append(node.right)
                
    
            output.append(temp_avg / q_len)
            temp_avg = 0
            q_len = 0
            
            for node in temp:
                q.put(node)
            
            temp = []
            
        
        return output
        
if __name__ == '__main__':
    obj = Solution()
    t7 = TreeNode(7)
    t15 = TreeNode(15)
    t20 = TreeNode(20, t15, t7)
    t9 = TreeNode(9)
    t3 = TreeNode(3, t9, t20)

    print(obj.averageOfLevels(t3))