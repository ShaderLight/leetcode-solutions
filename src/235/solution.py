from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x:int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_route = self.nodeRoute(root, p.val)
        q_route = self.nodeRoute(root, q.val)
        
        print(list(map(lambda x: x.val, p_route)))
        print(list(map(lambda x: x.val, q_route)))
        
        last_traced_node = root
        for i in range(1, (min(len(p_route), len(q_route)))):
            if p_route[i].val != q_route[i].val:
                return last_traced_node
            last_traced_node = p_route[i]
        
        return last_traced_node
    
    def nodeRoute(self, root:TreeNode, val:int) -> List[TreeNode]:
        route = [root]
        curr = root
        while curr.val != val:
            if curr.val > val:
                curr = curr.left
                route.append(curr)
            if curr.val < val:
                curr = curr.right
                route.append(curr)

        
        return route
        