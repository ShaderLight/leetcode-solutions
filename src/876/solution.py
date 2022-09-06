from __future__ import annotations
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        try:
            while head.next:
                mid, head = mid.next, head.next.next
        except AttributeError:
            pass
        
        return mid