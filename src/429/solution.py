from __future__ import annotations
import queue
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val:Optional[int]=None, children:Optional[List[Node]]=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        output: List[List[int]] = []
        q: queue.Queue[Node] = queue.Queue(10000)
        row_temp: List[int] = []
        next_row: List[Node] = []
        
        q.put(root)
        
        while not q.empty():
            while not q.empty():
                curr_node = q.get()
                assert curr_node.val
                
                if curr_node.children:
                    next_row += curr_node.children
                    
                row_temp.append(curr_node.val)
                
            output.append(row_temp)
            row_temp = []
                
            for o in next_row:
                q.put(o)
                
            next_row = []
                
            
        return output

