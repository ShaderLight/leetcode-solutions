
from typing import*
import sys

sys.setrecursionlimit(50) # For debugging purposes

class Node:
    def __init__(self, value: int, left_child, right_child, starting_index, ending_index) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.starting_index = starting_index
        self.ending_index = ending_index

class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.root = self.build(nums, 0, len(nums)-1)
        
    def halfIndex(self, li: int, ri: int) -> int:
        return (ri+li)//2
    
    def build(self, nums, li: int, ri: int) -> Node:
        if ri==li:
            return Node(nums[li], None, None, li, ri)

        h_ind = self.halfIndex(li,ri)
        
        print(f'Calling build within {li}:{h_ind}')
        left_child = self.build(nums, li, h_ind)
        print(f'Calling build within {h_ind+1}:{ri}')
        right_child = self.build(nums, h_ind+1, ri)
            
        return Node(left_child.value+right_child.value, left_child, right_child, li, ri)
    
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val

        self.updateUtil(self.root, index, diff)

    def updateUtil(self, curr_node: Node, index: int, diff: int) -> None:
        if index >= curr_node.starting_index and index <= curr_node.ending_index:
            curr_node.value += diff
            if curr_node.left_child:
                self.updateUtil(curr_node.left_child, index, diff)
                self.updateUtil(curr_node.right_child, index, diff)
        else:
            return

    def sumRange(self, left: int, right: int) -> int:
        if right > self.root.ending_index or left < 0:
            return -1

        return self.sumRangeUtil(self.root, left, right)

    def sumRangeUtil(self, curr_node: Node, li: int, ri: int) -> int:
        if (li <= curr_node.starting_index) and (ri >= curr_node.ending_index):
            return curr_node.value

        if (li > curr_node.ending_index or ri < curr_node.starting_index):
            return 0

        return self.sumRangeUtil(curr_node.left_child, li, ri) + self.sumRangeUtil(curr_node.right_child, li, ri)