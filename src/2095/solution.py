from __future__ import annotations
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        before_slow_ptr = None
        slow_ptr = head
        fast_ptr = head

        if fast_ptr.next != None:
            before_slow_ptr = head
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

            if fast_ptr.next:
                fast_ptr = fast_ptr.next

        while fast_ptr.next != None:
            before_slow_ptr = before_slow_ptr.next
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

            if fast_ptr.next:
                fast_ptr = fast_ptr.next


        before_slow_ptr.next = slow_ptr.next

        return head

def listToLinkedList(values: List[int]) -> ListNode:
    N = len(values)
    if N == 1:
        return ListNode(values[0])

    head = ListNode(values[0])
    ptr = head
    
    for i in range(1, N):
        ptr.next = ListNode(values[i])
        ptr = ptr.next

    return head


def linkedListToList(head: ListNode) -> List[int]:
    output: List[int] = [head.val]
    ptr = head

    while ptr.next:
        ptr = ptr.next
        output.append(ptr.val)

    return output


if __name__ == '__main__':
    obj = Solution()
    print(linkedListToList(obj.deleteMiddle(listToLinkedList([1,3,4,7,1,2,6]))))